from django.http import HttpResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Item, Registers


# Create your views here.
def index(request):
    return HttpResponse("BORELLI GADO")


list_salas = ['A101', 'B202', 'C305']
def salas(request):
    if request.method == "GET":
        dict = []
        for sala in list_salas:
            dict.append({"nome_sala": sala})

        json_response = json.dumps(dict) 

        return HttpResponse(json_response)
    else:
        return HttpResponse(404)

@csrf_exempt 
def add_item(request):
    """ Adds an item to the database
    :param:
    """
    if request.method == "POST":
        data = json.loads(request.body)
        item = Item(name=data['name'],
            barcode=data['barcode'],
            room=data['room']
        )
        item.save()
        return HttpResponse(f"ITEM {data['name']} INCLUIDO COM SUCESSO")

@csrf_exempt 
def delete_item(request, barcode):
    """ Deletes an item to the database
    :param:
    """
    if request.method == "POST":
        item = Item.objects.filter(barcode=barcode).all()

        if not item:
            return HttpResponse(json.dumps({"Erro": "Item nao encontrado"}))
        else:
            item.delete()
        return HttpResponse(f"ITEM COM CÓDIGO: {item['name']} DELTETADO COM SUCESSO")

def get_item(request, barcode):
    if request.method == "GET":
        item = Item.objects.filter(barcode=barcode).first()

        if not item:
            return HttpResponse(json.dumps({"Erro": "Item nao encontrado"}))
        else:
            obj = model_to_dict(item)
            return HttpResponse(json.dumps(obj))


@csrf_exempt 
def add_read(request):
    """ Adds an read to the database
    :param: barcode -> 
    """
    if request.method == "POST":
        data = json.loads(request.body)
        item = Item.objects.filter(barcode=data['barcode']).first()
        room = data['room']
        reg = Registers(
            item=item,
            room=room
        )
        reg.save()
        return HttpResponse(f"REGISTRO INCLUIDO COM SUCESSO")



@csrf_exempt 
def add_register(request):
    """ Adds an read to the database
    :param: barcode -> 
    """
    if request.method == "POST":
        data = json.loads(request.body)
        item = Item.objects.filter(barcode=data['barcode']).first()
        room = data['room']
        reg = Registers(
            item=item,
            room=room
        )
        reg.save()
        return HttpResponse(f"REGISTRO INCLUIDO COM SUCESSO")

@csrf_exempt 
def del_register(request, register_id):
    """ Deletes an read from the database
    :param: barcode -> 
    """
    if request.method == "POST":
        reg = Registers.objects.get(pk=register_id)
        reg.delete()
        return HttpResponse(f"REGISTRO EXCLUIDO COM SUCESSO")

def get_register_by_room(request, room_name):
    """
    https://amused-hedgehog-lovely.ngrok-free.app/api/room_register/A202/
    """
    if request.method == "GET":
        registers = Registers.objects.filter(room=room_name).all()

        if not registers:
            return HttpResponse(json.dumps({"Erro": "Registro nao encontrado"}))
        else:
            reg = []
            serialized_data = serialize("json", registers)
            serialized_data = json.loads(serialized_data)
            for data in serialized_data:
                item = Item.objects.get(pk=data["fields"]['item'])
                data["fields"]['item'] = model_to_dict(item)
                reg.append(data["fields"])

            return HttpResponse(json.dumps(reg))

def get_register_by_product(request, barcode):
    """
    https://amused-hedgehog-lovely.ngrok-free.app/api/product_register/3333333333/
    
    """
    if request.method == "GET":
        registers = Registers.objects.filter(item__barcode=barcode).all()

        if not registers:
            return HttpResponse(json.dumps({"Erro": "Registro nao encontrado"}))
        else:
            reg = []
            serialized_data = serialize("json", registers)
            serialized_data = json.loads(serialized_data)
            for data in serialized_data:
                item = Item.objects.get(pk=data["fields"]['item'])
                data["fields"]['item'] = model_to_dict(item)
                reg.append(data["fields"])

            return HttpResponse(json.dumps(reg))
