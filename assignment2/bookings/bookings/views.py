from rest_framework import viewsets
from .models import Movies
from .serializers import MovieSerializer
from .serializers import SeatSerializer
from .serializers import BookingSerializer
from django.shortcuts import render
from .models import Seats
from .models import Bookings


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seats.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = BookingSerializer

def base_view(request):
    return render(request, 'base.html')

def movies_view(request):
    movies = Movies.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

def seat_list_view(request):
    seats = Seats.objects.all().order_by('seatNumber')
    return render(request, 'seat_booking.html', {'seat': seats})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        seat = request.POST['seat_number']
        Booking.objects.create(user=request.user, movie=movie, seat_number=seat)
        return redirect('booking_history')
    return render(request, 'seat_booking.html', {'seat': seat})

def bookings_history_view(request):
    bookings = Bookings.objects.select_related('movie', 'seat').order_by('-bookingDate')
    return render(request, 'booking_history.html', {'bookings': bookings})