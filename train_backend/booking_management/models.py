import datetime

from django.db import models


class BookingDetails(models.Model):
    number_of_seats_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
    )
    date_of_booking = models.DateField(db_column="date_of_booking")
    coach_id = models.CharField(db_column='coach_id', max_length=10)
    number_of_seats = models.IntegerField(db_column='number_of_seats', choices=number_of_seats_choices)
    objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'booking_details'


class Seats(models.Model):
    date = models.DateField(db_column="date", default=datetime.date.today)
    seat_number = models.IntegerField(db_column='seat_number')
    booked_id = models.ForeignKey(BookingDetails, db_column='booked_id', related_name='booked_id',
                                  on_delete=models.CASCADE, null=True)
    is_booked = models.BooleanField(db_column='is_booked', default=False)
    objects = models.Manager()

    class Meta:
        managed = True
        db_table = 'seats'
        unique_together = ('date', 'seat_number')
