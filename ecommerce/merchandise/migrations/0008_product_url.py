# Generated by Django 3.0.8 on 2020-07-30 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0007_auto_20200730_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url',
            field=models.URLField(null=True),
        ),
    ]
