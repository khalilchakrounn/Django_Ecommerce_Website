from django.urls import path 
from . import views
app_name ='store'

from store.views import product_creat_view, aboutView, contact,dynamic_lookup

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('about/', aboutView),
    path('contact/', contact),
    path('create/',product_creat_view),
    path('products/<int:id>/', dynamic_lookup, name='product'), # would be better not to use due to url complexity
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
]
