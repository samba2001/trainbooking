# Generated by Django 3.2 on 2023-04-26 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_management', '0005_alter_seats_seat_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='seats',
            name='is_booked',
            field=models.BooleanField(db_column='is_booked', default=False),
        ),
    ]
