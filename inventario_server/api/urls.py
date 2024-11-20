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
   
    path("salas_listar/", views.salas_pesquisar, name="salas_listar"),
    path("sala_consultar/<str:room_id>/", views.sala_consultar, name="sala_consultar"),
     
    path("inventarios_pesquisar/", views.inventarios_pesquisar, name="inventarios_pesquisar"),
    path("inventario_consultar/<str:id_inventario>/", views.inventario_consultar, name="inventario_consultar"),
    path("inventario_incluir/", views.inventario_incluir, name="inventario_incluir"),
     
    path("items_listar/", views.items_listar, name="items_listar"),
    path("item_consultar/<str:barcode>/", views.item_consultar, name="item_consultar"),
    path("item_deletar/<str:barcode>/", views.item_deletar, name="item_deletar"),
    path("item_incluir/", views.item_incluir, name="item_incluir"),
    
    path("registros_listar/", views.registros_listar, name="registros_listar"),
    path("registro_incluir/", views.registro_incluir, name="registro_incluir"),
    path("registro_deletar/<str:id>/", views.item_deletar, name="item_deletar"),


    path("add_register/", views.add_register, name="add_register"),
    path("product_register/<str:barcode>/", views.get_register_by_product, name="get_register_by_product"),
    path("room_register/<str:room_name>/", views.get_register_by_room, name="get_register_by_room"),
    #path("del_register/<str:id>/", views.delete_register, name="delete_register"),
    
]