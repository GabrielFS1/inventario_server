from django.core.management.base import BaseCommand
from api.models import Room, Item, Inventory, Registers

import random

class Command(BaseCommand):
    help = 'Populate the database with fictitious data'

    def handle(self, *args, **kwargs):
        # Create Rooms
        room_names = ["Living Room", "Bedroom", "Kitchen", "Bathroom", "Office"]
        rooms = [Room.objects.create(name=name) for name in room_names]

        # Create Items
        item_names = ["Chair", "Table", "Lamp", "Sofa", "Bed"]
        items = []
        for i, name in enumerate(item_names):
            room = random.choice(rooms)
            barcode = f"0000{i+1}"
            items.append(Item.objects.create(name=name, barcode=barcode, room=room))
    
        # Create Inventories
        inventory_names = ["First Inventory", "Second Inventory", "Third Inventory"]
        inventories = [Inventory.objects.create(name=name) for name in inventory_names]

        # Create Registers
        authors = ["Alice", "Bob", "Charlie", "Dave", "Eve"]
        for item in items:
            room = item.room
            inventory = random.choice(inventories)
            author = random.choice(authors)
            Registers.objects.create(item=item, room=room, inventory=inventory, author=author)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fictitious data'))
