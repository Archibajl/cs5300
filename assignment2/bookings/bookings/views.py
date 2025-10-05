from rest_framework import viewsets
from rest_framework import generics
from .serializers import MovieSerializer
from .serializers import SeatSerializer
from .serializers import BookingSerializer
from django.shortcuts import render
from .models import Movies
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

# def seat_booking(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#     if request.method == 'POST':
#         seat = request.POST['seat_number']
#         Booking.objects.create(user=request.user, movie=movie, seat_number=seat)
#         return redirect('booking_history')
#     return render(request, 'seat_booking.html', {'seat': seat})

def bookings_history_view(request):
    bookings = Bookings.objects.select_related('movie', 'seat').order_by('-bookingDate')
    return render(request, 'booking_history.html', {'bookings': bookings})

class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    def get_queryset(self):
        try:
            return Movies.objects.all()
        except Exception as e:
            print("DB Error:", e)
            return Movies.objects.none()

# List all seats and their availability
class SeatListView(generics.ListAPIView):
    serializer_class = SeatSerializer
    def get_queryset(self):
        try:
            return Seats.objects.all()
        except Exception as e:
            print("DB Error:", e)
            return Seats.objects.none()

# List all bookings
class BookingListView(generics.ListAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        try:
            return Bookings.objects.select_related('movie', 'seat').all()
        except Exception as e:
            print("DB Error:", e)
            return Bookings.objects.none()

# Create a new booking
class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    def get_queryset(self):
        try:
            return Bookings.objects.all()
        except Exception as e:
            print("DB Error:", e)
            return Bookings.objects.none()

