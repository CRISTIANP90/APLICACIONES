# Generated by Django 5.1.1 on 2024-09-14 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_id', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
                ('direccion', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_id', models.CharField(max_length=60)),
                ('id_cliente', models.CharField(max_length=60)),
                ('id_producto', models.CharField(max_length=60)),
                ('Id_domiciliario', models.CharField(max_length=60)),
            ],
        ),
    ]
