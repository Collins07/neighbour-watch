# Generated by Django 3.2.2 on 2022-06-19 00:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbour', '0006_auto_20220619_0349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='price',
        ),
    ]
