from rest_framework import viewsets, serializers
from .models import Movies
from .models import Seats
from .models import Bookings
from rest_framework import serializers
from .models import Movies, Seats, Bookings

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['id', 'title', 'description', 'releaseDate', 'duration']

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = ['id', 'seatNumber', 'bookingStatus', 'published']

class BookingSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    seat = SeatSerializer(read_only=True)
    class Meta:
        model = Bookings
        fields = ['id', 'movie', 'seat', 'bookingDate']
        
