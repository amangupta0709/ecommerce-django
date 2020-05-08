from django.shortcuts import render, get_object_or_404
from .models import Items, CartItems
from django.db.models import F, Sum
from django import template

productdata = Items.objects.all().annotate(discountedprice = F('price') - (F('price')*F('discount')/100)).order_by('id')


def cartlist(request):
    if request.method == 'POST':
        if 'addtocartbtn' in request.POST:
            id = request.POST['addtocartbtn']
            id = int(id)
            addtocart(id,1)
        elif 'delete' in request.POST:
            id = request.POST['delete']
            id = int(id)
            deletecartitem(id)
    
    cartidlist = list(CartItems.objects.all().values_list('cartitem', flat=True))
    if CartItems.objects.count()==0:
        cartlist.context = {
            'cartvalues':CartItems.objects.all(),
            'discounttotalprice': 0,
            'count': CartItems.objects.count(),
        }
    else:
        producttotalprice,producttotaldiscountprice = 0,0
        for i in CartItems.objects.all().values_list('cartitem__id', flat=True):
            producttotalprice += CartItems.objects.get(cartitem__id=i).cartitem.price * CartItems.objects.get(cartitem__id=i).quantity
            producttotaldiscountprice += productdata.get(id=i).discountedprice * CartItems.objects.get(cartitem__id=i).quantity
        cartlist.context = {
            'cartvalues':CartItems.objects.all(),
            'count': CartItems.objects.count(),
            #'totalprice': format(CartItems.objects.all().aggregate(Sum('cartitem__price'))['cartitem__price__sum'], ',d'),
            #'discounttotalprice': format(productdata.filter(id__in = cartidlist).aggregate(Sum('discountedprice'))['discountedprice__sum'], ',d')
            'totalprice': format(producttotalprice, ',d'),
            'discounttotalprice': format(producttotaldiscountprice, ',d')
        }
    
    #return render(request, 'base.html', cartlist.context)


def allitems(request):
    cartlist(request)
    context = {
        'cartitems':cartlist.context,
        'productdata':productdata
    }
    return render(request, 'index.html', context)

    

def itemlist(request, category):
    cartlist(request)
    categorydata = productdata.filter(category=category)

    context = {
        'cartitems':cartlist.context,
        'productdata':categorydata
    }
    
    return render(request, 'index.html', context)

def addtocart(id, quantity):
    cartitem = Items.objects.get(id=id)
    newid = CartItems.objects.count()+1
    if not CartItems.objects.filter(cartitem__id = id).exists():
        if not CartItems.objects.count() == 0:
            for i in range(1,CartItems.objects.latest('id').id + 1):
                if not CartItems.objects.filter(id=i).exists():
                    newid = i
                    break

        cartitemdata = CartItems.objects.create(id=newid ,title=cartitem.title,cartitem=cartitem, quantity=int(quantity))

    else:
        qty = CartItems.objects.get(cartitem__id = id)
        qty.quantity += int(quantity)
        qty.save()

def deletecartitem(id):
    item = CartItems.objects.get(id=id)
    item.delete()
    
    

def productview(request, category, slugname):
    details = productdata.filter(category=category).get(slug=slugname)
    if request.method == "POST" and 'itemquantity' in request.POST:
        # if CartItems.objects.filter(cartitem=details).exists():
        #     qty = CartItems.objects.get(cartitem=details)
        #     qty.quantity = request.POST['itemquantity']
        #     qty.save()
        # else:
        #     addtocart()
        qty = request.POST['itemquantity']
        id = details.id
        addtocart(id,qty)
        
    cartlist(request)
    context = {
        'cartitems':cartlist.context,
        'details': details,
        'urlmap': request.path.split('/')[1:]
    }
    return render(request, 'productdetail.html', context)
