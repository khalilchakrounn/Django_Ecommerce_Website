from itertools import product
from unicodedata import category
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render,redirect
from .models import Category, Product
from django.http import Http404 
# Create your views here.
from .form import ProductForm, RawProductForm

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


#def product_creat_view(request):
    #new_name=request.POST.get('name')   # to get the name from the request
    form= ProductForm(request.Post or None)
    if form.is_valid():
        form.save()
        form= ProductForm()  # to clear the form and represent an empty one

    context={
        'form': form
    }
    return render ( request, "store/products/create.html", context)


def product_creat_view(request):
    form= RawProductForm()
    if request.method =="POST":
        form= RawProductForm(request.Post )
        if form.is_valid():
            form.save()
            Product.objects.create(**form.cleaned_data)   # ** to turn the the inputs to Kwargs
           
        else:
            print(form.errors)
             #form= ProductForm()  # to clear the form and represent an empty one
    context={
        'form': form
    }
    return render ( request, "store/products/create.html", context)


def render_intial_data(request):
    initial_data={
        'slug': "slug name"
    }
    #obj=Product.objects.get(id=1)#for modification
    Form=ProductForm(request.POST or None, initial=initial_data) # instance=obj   put instead of initial data for modification
    if Form.is_valid():
        Form.save()
    context = {
        'form': Form
    }
    return render(request, "products/product_create.html", context)

def dynamic_lookup(request,id):
    try:
        obj=Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    #obj=get_object_or_404(Product, id=id)
    context={
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj= get_object_or_404(Product, id=id)
    if request.method =="POST":
        obj.delete()
        return redirect('../../')
    context={
        "object": obj
    }
    return render(request, "products/product_delete.html", context)