# Generated by Django 5.0.4 on 2024-04-07 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0002_order_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
