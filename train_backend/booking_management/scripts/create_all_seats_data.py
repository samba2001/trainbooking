import sys

sys.path.insert(0, '.')
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'train_backend.settings')
import django

django.setup()

from booking_management.models import Seats

bulk_create_objects = []
for each_seat in range(1, 81):
    bulk_create_objects.append(Seats(seat_number=each_seat))
Seats.objects.bulk_create(bulk_create_objects)
