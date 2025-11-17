from django.contrib import admin
from django.urls import path
from listings.views import ListingListView, BookingListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("listings/", ListingListView.as_view()),
    path("bookings/", BookingListView.as_view()),
]
