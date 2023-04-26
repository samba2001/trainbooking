from django.urls import path
from booking_management.views import BookTickets

urlpatterns = [
    path('', BookTickets.as_view(), name='book_tickets'),
]
