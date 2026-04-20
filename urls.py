from django.urls import path
from . import views

urlpatterns = [

    path('', views.product_list, name='product_list'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete-product/<int:id>/', views.delete_product, name='delete_product'),

    path('add-customer/', views.add_customer, name='add_customer'),
    path('add-order/', views.add_order, name='add_order'),
    path('orders/', views.order_list, name='order_list'),

    # API
    path('api/product/create/', views.product_create_api),
    path('api/product/update/<int:id>/', views.product_update_api),
    path('api/product/delete/<int:id>/', views.product_delete_api),
]

"""
URL configuration for ecommerce_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

