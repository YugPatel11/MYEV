# Generated by Django 5.1.6 on 2025-04-09 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_booking_feedback'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking',
            new_name='Bookings',
        ),
    ]
