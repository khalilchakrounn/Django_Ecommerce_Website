from itertools import product
from unicodedata import category
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import Category, Product
# Create your views here.

def categories(request):
    return{
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()# select* query
    return render(request, 'store/home.html',{'products': products})


def product_detail(request , slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category.slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category})

def contact(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, 'store/contacts.html', {'args': args})

def aboutView(request, *args, **kwargs):
    my_context={
        "text" : "this is the text",
        "number": 1212
    }
    return render(request, 'store/about.html', my_context)