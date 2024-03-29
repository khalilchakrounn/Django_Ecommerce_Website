from audioop import reverse
from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255,unique=True)
    #in the database there should only be one slug 
    #slug is used so that we can write the name of the category in the url and so that that category name is unique 

    class Meta:
        verbose_name_plural = 'categories'


    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name;


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    authr = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    #pip isntall Pillow to use images
    #/images inside /Media
    slug = models.SlugField(max_length=255)
    price= models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    in_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    #default time of creation
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural ='Products'
        ordering = ('-created',)
        #when selected , retrivve ordered by creation date
    
    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])# store from the name space chosen in urls
    

    def __str__(self):
        return self.title;




#venv2\Scripts\activate
#py manage.py makemigrations
#py manage.py migrate