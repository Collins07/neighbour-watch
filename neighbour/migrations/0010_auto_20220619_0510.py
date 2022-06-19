# Generated by Django 3.2.2 on 2022-06-19 02:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('neighbour', '0009_userprofile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighbourhood',
            name='admin',
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighborhood', to=settings.AUTH_USER_MODEL),
        ),
    ]
