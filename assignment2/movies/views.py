from rest_framework import viewsets
from .models import Movie
from .serializers import MovieSerializer
from .serializers import SeatSerializer
from .serializers import BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = BookingSerializer

def movie_view(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/templates/movie_list.html', {'movies': movies})

# views.py
from django.shortcuts import render
from .models import Seat

def seat_list_view(request):
    seats = Seat.objects.all().order_by('seatNumber')
    return render(request, 'yourapp/seat_list.html', {'seats': seats})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'POST':
        seat = request.POST['seat_number']
        Booking.objects.create(user=request.user, movie=movie, seat_number=seat)
        return redirect('booking_history')
    return render(request, 'bookings/templates/seat_booking.html', {'seat': Seat})

def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/templates/booking_history.html', {'bookings': bookings})
