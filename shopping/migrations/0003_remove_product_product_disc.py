# Generated by Django 3.2.16 on 2022-12-11 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_category_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_disc',
        ),
    ]
