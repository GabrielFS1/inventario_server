

```
class Item(models.Model):
    name = models.CharField(max_length=120),
    barcode = models.CharField(max_length=120),
    room = models.CharField(max_length=120)
```


```
class Registers(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE),
    room = models.CharField(max_length=120),
    date = models.DateField(default=datetime.datetime.now)
```



Requests

* Adicionar Item no banco de dados
- Comando para cadastrar itemns

POST/ https://amused-hedgehog-lovely.ngrok-free.app/api/add_item/
json = {
    "name" : "ADWHUHGAIOWHD",
    "barcode": 27937812769348712,
    "room": "A202"
}

* Consultar Item no banco de dados

GET/ amused-hedgehog-lovely.ngrok-free.app/api/item/<barcode>/

retorna {"id": 7, "name": "33333333333", "barcode": "3333333333", "room": "A202"}

* Incluir Registro no banco de dados
Deve ser incluido quando o usuario faz uma leitura do código de barras para salvar a leitura
json = {
    "barcode": 11111111,
    "room": "A202"
}

POST/ https://amused-hedgehog-lovely.ngrok-free.app/api/add_register/

* Consultar todos os Registro de uma sala
GET/    https://amused-hedgehog-lovely.ngrok-free.app/api/room_register/romm_name/
retorna 
    [{"item": {"id": 6, "name": "1111111111", "barcode": "11111111", "room": "A202"},
     "room": "A202", "date": "2023-10-18"}  ...] 
     
* Consultar todos os Registro de um produto
GET/    https://amused-hedgehog-lovely.ngrok-free.app/api/room_register/barcode/
retorna [{"item": {"id": 7, "name": "33333333333", "barcode": "3333333333", "room": "A202"},
         "room": "A202", "date": "2023-10-18"}...]