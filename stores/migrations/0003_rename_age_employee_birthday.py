# Generated by Django 4.2.2 on 2023-06-20 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0002_store_location_store_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='age',
            new_name='birthday',
        ),
    ]
