# Generated by Django 4.1.2 on 2023-04-21 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_table', '0003_rename_product_id_detailtable_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailtable',
            old_name='product',
            new_name='product_id',
        ),
    ]
