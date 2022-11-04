from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
#the slug field is named automatically with the name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','authr','slug','price','in_stock','created','updated']
    list_filter = ['in_stock','in_active']
    list_editable = ['price','in_stock']
    prepopulated_fields = {'slug': ('title',)}






#py manage.py createsuperuser    