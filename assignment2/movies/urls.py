from django.urls import path
from .views import seat_list_view

urlpatterns = [
    path('seats/', seat_list_view, name='seat_bookings'),
]