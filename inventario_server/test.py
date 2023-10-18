import requests

def add_item(d):

    r = requests.post("https://amused-hedgehog-lovely.ngrok-free.app/api/add_item/", json=d)

def add_register(d):

    r = requests.post("https://amused-hedgehog-lovely.ngrok-free.app/api/add_register/", json=d)



def del_item():
    r = requests.post("https://amused-hedgehog-lovely.ngrok-free.app/api/del_item/27937812769348712/")
    print(r)

d = {
    "name" : "ADWHUHGAIOWHD",
    "barcode": 27937812769348712,
    "room": "A202"
}
#add_item(d)

d = {
    "name" : "1111111111",
    "barcode": 11111111,
    "room": "A202"
}
#add_item(d)
d = {
    "name" : "33333333333",
    "barcode": 3333333333,
    "room": "A202"
}


d = {
    "barcode": 3333333333,
    "room": "A202"
}
add_register(d)     

d = {
    "barcode": 11111111,
    "room": "A202"
}
#add_register(d)     
#add_item()
#del_item()