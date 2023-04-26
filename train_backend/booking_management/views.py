from rest_framework.views import APIView, Response, status
from booking_management.managers.booking_details_manager import BookingDetailsManager


class BookTickets(APIView):
    @staticmethod
    def post(request):
        try:
            data = request.data
            BookingDetailsManager.create_booking_details(data)
            return Response("Success", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetSeatDetails(APIView):
    @staticmethod
    def get(request):
        try:
            data = BookingDetailsManager.get_all_seats()
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
