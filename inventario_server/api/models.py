from django.db import models
import datetime

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=120)
    barcode = models.CharField(max_length=120)
    room = models.CharField(max_length=120)

class Registers(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    room = models.CharField(max_length=120)
    date = models.DateTimeField(default=datetime.now, blank=True)



