from django.urls import path 
from . import views
app_name ='store'

from store.views import product_creat_view, aboutView, contact

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('about/', aboutView),
    path('contact/', contact),
    path('create/',product_creat_view),
]
