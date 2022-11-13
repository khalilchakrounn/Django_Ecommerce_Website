"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from store import views



urlpatterns = [
    path('admin/', admin.site.urls),   
    path('blog/', include('blog.urls')),
    path('', include('store.urls',namespace='store')),#to be more organised and to include urls from store urls
    path('courses/', include('courses.urls')),
    path('products/', include('products.urls')),
    #path('', home_view, name='home'),
    #path('about/<int:id>/', about_view, name='product-detail'),
    #path('contact/', contact_view),
]
#for debugging
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)




#all urls definitions, admin urls, others ...
#item name seperate