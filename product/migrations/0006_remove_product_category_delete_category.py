# Generated by Django 4.0.5 on 2023-01-17 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_remove_product_detail_remove_product_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]