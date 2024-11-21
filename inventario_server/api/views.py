from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.core.serializers import serialize
import json
from django.shortcuts import get_object_or_404
from .models import Inventory, Item, Registers, Room
from django.core import serializers


def index(request):
    return HttpResponse("BORELLI GADO")


@csrf_exempt
def salas_pesquisar(request):
    """Returns a list of rooms"""
    if request.method == "GET":
        limit = request.GET.get('limit', 3)
        try:
            limit = int(limit)
        except ValueError:
            return JsonResponse({"error": "Invalid limit parameter"}, status=400)

        rooms = Room.objects.all()[:limit]
        
        rooms_list = list(rooms.values())  # Convert queryset to list of dictionaries
        
        return JsonResponse(rooms_list, safe=False)  # Return as JSON response 
    else:
        return HttpResponse(status=403)


@csrf_exempt
def sala_consultar(request, room_id):
    """Returns a single room by ID"""
    if request.method == "GET":
        try:
            room = Room.objects.get(pk=room_id)
        except Room.DoesNotExist:
            return JsonResponse({"error": "Room not found"}, status=404)

        room = model_to_dict(room)
        
        data = json.dumps(room)
        
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse(status=403)


@csrf_exempt
def sala_incluir(request):
    """Inserts a new room"""
    if request.method == "POST":
        data = json.loads(request.body)
        room = Room(name=data['name'])
        room.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=403)


@csrf_exempt
def items_listar(request):
    """Returns a list of items"""
    if request.method == "GET":
        limit = request.GET.get('limit', 50)
        try:
            limit = int(limit)
        except ValueError:
            return JsonResponse({"error": "Invalid limit parameter"}, status=400)

        items = Item.objects.all()[:limit]

        data = []

        for item in items:
            data.append({"id": item.id, "name": item.name, "barcode": item.barcode, "room": item.room.name})

        data = json.dumps(data)

        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse(status=403)


@csrf_exempt
def item_consultar(request, barcode):
    """Returns a single item by barcode"""
    if request.method == "GET":
        item = Item.objects.filter(barcode=barcode).first()
        if not item:
            return JsonResponse({"error": "Item not found"}, status=404)

        obj = model_to_dict(item)
        return JsonResponse(obj)
    else:
        return HttpResponse(status=403)


@csrf_exempt
def item_deletar(request, barcode):
    """Deletes an item by barcode"""
    if request.method == "DELETE":
        item = Item.objects.filter(barcode=barcode).first()
        if not item:
            return JsonResponse({"error": "Item not found"}, status=404)

        item.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)


@csrf_exempt
def item_incluir(request):
    """Inserts a new item"""
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            room = Room.objects.get(pk=data['room'])
        except Room.DoesNotExist:
            return JsonResponse({"error": "Room not found"}, status=404)

        item = Item(name=data['name'], barcode=data['barcode'], room=room)
        
        item.save()
        
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)


@csrf_exempt
def registros_listar(request):
    """Returns a list of registers"""
    if request.method == "GET":
        registers = Registers.objects.all()
        data = []
        for register in registers:
            data.append({
                "id": register.id,
                "item": register.item.name,
                "room": register.room.name,
                "inventory": register.inventory.name,
                "author": register.author,
                "date": register.date.isoformat()}
            )
        data = json.dumps(data)

        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse(status=403)


@csrf_exempt
def registro_incluir(request):
    """Inserts a new register"""
    """Parameters:
    {
        "barcode": "123",
        "room": 1,
        "inventory": 1,
        "author": "John Doe"
    }
    """
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            item = Item.objects.filter(barcode=data['barcode']).first()
            room = Room.objects.get(pk=data['room'])
            inventory = Inventory.objects.get(pk=data['inventory'])
        except (Item.DoesNotExist, Room.DoesNotExist, Inventory.DoesNotExist):
            return JsonResponse({"error": "Item, Room or Inventory not found"}, status=404)

        reg = Registers(
            item=item,
            room=room,
            inventory=inventory,
            author=data.get('author', '')
        )
        reg.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=403)


@csrf_exempt
def registro_deletar(request, register_id):
    """Deletes a register by ID"""
    if request.method == "DELETE":
        try:
            reg = Registers.objects.get(pk=register_id)
        except Registers.DoesNotExist:
            return JsonResponse({"error": "Register not found"}, status=404)

        reg.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)

#========================================
# INVENTARIO 
@csrf_exempt
def inventarios_pesquisar(request):
    """Returns a list of inventories"""
    if request.method == "GET":
        inventories = Inventory.objects.all()
        data = []
        for inventory in inventories:
            data.append({"id": inventory.id, "name": inventory.name, "date": inventory.date.isoformat()})

        serialized_inventories = json.dumps(data)
        return HttpResponse(serialized_inventories, content_type='application/json')
    else:
        return HttpResponse(status=403)

@csrf_exempt
def inventario_consultar(request, id_inventario):
    """Returns a single inventory by ID"""
    if request.method == "GET":
        inventory = get_object_or_404(Inventory, pk=id_inventario)
        data = {"id": inventory.id, "name": inventory.name, "date": inventory.date.isoformat()}
        serialized_inventory = json.dumps(data)
        return HttpResponse(serialized_inventory, content_type='application/json')
    else:
        return HttpResponse(status=403)

@csrf_exempt
def inventario_incluir(request):
    """Inserts a new inventory"""
    if request.method == "POST":
        data = json.loads(request.body)
        inventory = Inventory(name=data['name'])
        inventory.save()
        return JsonResponse({'id': inventory.id}, status=201)
    else:
        return HttpResponse(status=403)

@csrf_exempt
def inventario_atualizar(request, id_inventario):
    """Updates an existing inventory by ID"""
    if request.method == "PUT":
        data = json.loads(request.body)
        inventory = get_object_or_404(Inventory, pk=id_inventario)
        inventory.name = data.get('name', inventory.name)
        inventory.save()
        return JsonResponse({'id': inventory.id}, status=200)
    else:
        return HttpResponse(status=403)

@csrf_exempt
def inventario_deletar(request, id_inventario):
    """Deletes an inventory by ID"""
    if request.method == "DELETE":
        inventory = get_object_or_404(Inventory, pk=id_inventario)
        inventory.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=403)
    
#========================================
@csrf_exempt
def add_item(request):
    """Adds an item to the database"""
    if request.method == "POST":
        data = json.loads(request.body)
        item = Item(
            name=data['name'],
            barcode=data['barcode'],
            room_id=data['room']
        )
        item.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=403)


def get_item(request, barcode):
    """Gets an item by barcode"""
    if request.method == "GET":
        item = Item.objects.filter(barcode=barcode).first()
        if not item:
            return JsonResponse({"error": "Item not found"}, status=404)

        obj = model_to_dict(item)
        return JsonResponse(obj)
    else:
        return HttpResponse(status=403)


@csrf_exempt
def add_read(request):
    """Adds a read to the database"""
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            item = Item.objects.get(barcode=data['barcode'])
            room = Room.objects.get(pk=data['room'])
        except (Item.DoesNotExist, Room.DoesNotExist):
            return JsonResponse({"error": "Item or Room not found"}, status=404)

        reg, created = Registers.objects.update_or_create(
            item=item,
            room=room
        )
        return HttpResponse("REGISTRO INCLUIDO COM SUCESSO", status=201)
    else:
        return HttpResponse(status=403)


@csrf_exempt
def add_register(request):
    """Adds a register to the database"""
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            item = Item.objects.get(barcode=data['barcode'])
            room = Room.objects.get(pk=data['room'])
        except (Item.DoesNotExist, Room.DoesNotExist):
            return JsonResponse({"error": "Item or Room not found"}, status=404)

        reg = Registers(
            item=item,
            room=room
        )
        reg.save()
        return HttpResponse("REGISTRO INCLUIDO COM SUCESSO", status=201)
    else:
        return HttpResponse(status=403)


@csrf_exempt
def del_register(request, register_id):
    """Deletes a register by ID"""
    if request.method == "DELETE":
        try:
            reg = Registers.objects.get(pk=register_id)
        except Registers.DoesNotExist:
            return JsonResponse({"error": "Register not found"}, status=404)

        reg.delete()
        return HttpResponse("REGISTRO EXCLUIDO COM SUCESSO", status=204)
    else:
        return HttpResponse(status=403)


def get_register_by_room(request, room_name):
    """Gets registers by room name"""
    if request.method == "GET":
        registers = Registers.objects.filter(room__name=room_name).all()
        if not registers:
            return JsonResponse({"error": "Registro nao encontrado"}, status=404)

        reg = []
        serialized_data = serialize("json", registers)
        serialized_data = json.loads(serialized_data)
        for data in serialized_data:
            item = Item.objects.get(pk=data["fields"]['item'])
            data["fields"]['item'] = model_to_dict(item)
            reg.append(data["fields"])

        return JsonResponse(reg, safe=False)
    else:
        return HttpResponse(status=403)


def get_register_by_product(request, barcode):
    """Gets registers by product barcode"""
    if request.method == "GET":
        registers = Registers.objects.filter(item__barcode=barcode).all()
        if not registers:
            return JsonResponse({"error": "Registro nao encontrado"}, status=404)

        reg = []
        serialized_data = serialize("json", registers)
        serialized_data = json.loads(serialized_data)
        for data in serialized_data:
            item = Item.objects.get(pk=data["fields"]['item'])
            data["fields"]['item'] = model_to_dict(item)
            reg.append(data["fields"])

        return JsonResponse(reg, safe=False)
    else:
        return HttpResponse(status=403)
