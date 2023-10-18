"""
URL configuration for ecovendas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("salas/", views.salas, name="salas"),
   
    path("add_item/", views.add_item, name="add_item"),
    path("item/<str:barcode>/", views.get_item, name="get_item"),
    path("del_item/<str:barcode>/", views.delete_item, name="delete_item"),
    
    path("add_register/", views.add_register, name="add_register"),
    path("product_register/<str:barcode>/", views.get_register_by_product, name="get_register_by_product"),
    path("room_register/<str:room_name>/", views.get_register_by_room, name="get_register_by_room"),
    #path("del_register/<str:id>/", views.delete_register, name="delete_register"),
    
]