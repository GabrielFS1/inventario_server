# Generated by Django 4.2.6 on 2023-10-18 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_item_room_alter_registers_room_delete_room'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='local',
            new_name='room',
        ),
    ]
