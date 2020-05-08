from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import F
from django.utils.text import slugify


# Create your models here.
class Items(models.Model):
    title = models.CharField(max_length=30)
    CATEGORY_CHOICES = (
        ('Laptops','Laptops'),
        ('Smartphones','Smartphones'),
        ('Cameras','Cameras'),
        ('Accessories','Accessories')
    )
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=20)
    price = models.IntegerField()
    discount = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(100), MinValueValidator(0)]
    )
    ratings = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(5), MinValueValidator(0)]
    )
    
    productnew = models.BooleanField(default=False)
    image = models.ImageField(upload_to='Images/', default='Images/no-image')
    slug = models.SlugField(max_length=100, unique=True, default='no-slug')

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Items.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if self.slug == 'no-slug':
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

class CartItems(models.Model):
    title = models.CharField(max_length=30)
    cartitem = models.ForeignKey(Items, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.title


