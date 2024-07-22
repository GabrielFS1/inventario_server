import requests

def add_item(d):

    r = requests.post("https://amused-hedgehog-lovely.ngrok-free.app/api/add_item/", json=d)

def add_register(d):

    r = requests.post("https://amused-hedgehog-lovely.ngrok-free.app/api/add_register/", json=d)



def del_item():
    r = requests.post("https://amused-hedgehog-lovely.ngrok-free.app/api/del_item/27937812769348712/")
    print(r)

d = {
    "name" : "33333333333",
    "barcode": 3333333333,
    "room": "A202"
}
#add_item(d)


d = {
    "barcode": 3333333333,
    "room": "A202"
}
#add_register(d)     