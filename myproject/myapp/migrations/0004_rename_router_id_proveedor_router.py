# Generated by Django 5.1.2 on 2024-10-25 18:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_router_proveedor_router_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proveedor',
            old_name='router_id',
            new_name='router',
        ),
    ]
