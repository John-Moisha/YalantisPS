# Generated by Django 3.2 on 2021-05-01 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0004_categoty'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoty',
            new_name='Catalog',
        ),
    ]
