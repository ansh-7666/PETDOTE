# Generated by Django 4.1.2 on 2022-10-13 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20190330_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='items_json',
        ),
    ]
