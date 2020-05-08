from django.urls import path
from .views import itemlist, allitems, cartlist, productview

urlpatterns = [
    path('', allitems, name='home'),
    path('<str:category>', itemlist, name='categoryview'),
    path('<str:category>/<slug:slugname>', productview, name='itemdetail')
]
