# Generated by Django 4.0.5 on 2022-06-22 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_rename_detal_product_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='등록일자'),
        ),
    ]
