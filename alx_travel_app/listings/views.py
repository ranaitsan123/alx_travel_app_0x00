from rest_framework import generics
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer

class ListingListView(generics.ListAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingListView(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
