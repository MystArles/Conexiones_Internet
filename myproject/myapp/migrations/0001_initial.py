# Generated by Django 5.1.2 on 2024-10-22 20:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Router',
            fields=[
                ('router_id', models.AutoField(primary_key=True, serialize=False)),
                ('departamento', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=100)),
                ('tecnologia', models.CharField(max_length=100)),
                ('segmento', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('velocidad', models.CharField(max_length=100)),
                ('conexiones', models.IntegerField()),
                ('router', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.router')),
            ],
        ),
    ]
