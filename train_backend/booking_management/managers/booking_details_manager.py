import datetime

from django.db.models import Prefetch
from django.db import transaction

from booking_management.models import BookingDetails, Seats


class BookingDetailsManager:

    @staticmethod
    def get_booking_details():
        prefetch_related = Prefetch('seats', queryset=Seats.objects.all())
        return BookingDetails.objects.prefetch_related(prefetch_related).filter(coach_id="B1",
                                                                                date_of_booking=datetime.date.today())

    @staticmethod
    def get_available_seats():
        return Seats.objects.filter(date=datetime.date.today(), is_booked=False)

    @staticmethod
    def get_all_seats():
        return Seats.objects.filter(date=datetime.date.today()).values('date', 'seat_number', 'is_booked')

    @staticmethod
    def get_seat_object_by_seat_numbers(seat_numbers):
        return Seats.objects.filter(date=datetime.date.today(), seat_number__in=seat_numbers)

    @staticmethod
    def create_booking_details(data):
        selected_seats = data.get('selectedSeats').split(',')
        number_of_seats = len(selected_seats)
        selected_seats_objects = BookingDetailsManager.get_seat_object_by_seat_numbers(selected_seats)
        available_seats = BookingDetailsManager.get_available_seats()
        available_seats_list = available_seats.values_list('seat_number', flat=True)
        if len(available_seats_list) < number_of_seats:
            raise Exception('Available Seats are less than requested number of seats')

        with transaction.atomic():
            booking_object = BookingDetails(coach_id='B1', date_of_booking=datetime.date.today(),
                                            number_of_seats=number_of_seats)
            booking_object.save()
            bulk_update_seats = []
            for each_seat in selected_seats_objects:
                each_seat.booked_id = booking_object
                each_seat.is_booked = True
                bulk_update_seats.append(each_seat)
            Seats.objects.bulk_update(bulk_update_seats, fields=['booked_id', 'is_booked'])
