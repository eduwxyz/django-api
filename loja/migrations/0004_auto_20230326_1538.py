# Generated by Django 3.0.7 on 2023-03-26 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_auto_20230326_1533'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PedidoTipo',
            new_name='ProdutoTipo',
        ),
    ]
