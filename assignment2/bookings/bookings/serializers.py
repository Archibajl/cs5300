from rest_framework import viewsets, serializers
from .models import Movies
from .models import Seats
from .models import Bookings
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = '__all__'  # Or list specific fieds like ['title', 'genre']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'  # Or specify fields like ['user', 'movie', 'seat', 'bookingStatus']

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = '__all__'  # Or specify fields like ['row', 'number', 'isAvailable']
