# Generated by Django 4.2.2 on 2023-06-25 00:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0017_remove_store_owner_store_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='owner',
        ),
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
