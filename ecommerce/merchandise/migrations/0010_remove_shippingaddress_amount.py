# Generated by Django 3.0.8 on 2020-07-31 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0009_auto_20200730_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='amount',
        ),
    ]
