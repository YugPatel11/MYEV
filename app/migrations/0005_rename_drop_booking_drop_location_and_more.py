# Generated by Django 5.1.6 on 2025-04-19 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_bookings_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='drop',
            new_name='drop_location',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='pickup',
            new_name='pickup_location',
        ),
    ]
