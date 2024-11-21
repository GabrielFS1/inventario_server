from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=120)
    barcode = models.CharField(max_length=120, unique=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Registers(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, default=1)
    author = models.CharField(max_length=120, blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.item.name} in {self.room.name} by {self.author} on {self.date}"
