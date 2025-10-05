from django.test import TestCase
from bookings.models import Movies, Seats, Bookings
from bookings.serializers import MovieSerializer, SeatSerializer, BookingSerializer
from datetime import date
from datetime import timedelta

class SerializerTests(TestCase):
    def setUp(self):
        self.movie = Movies.objects.create(
            title="Interstellar",
            description="A mind-bending thriller",
            releaseDate=date(2010, 7, 16),
            duration=timedelta(minutes=148)
        )
        self.seat = Seats.objects.create(
            seatNumber="B2",
            bookingStatus=True,
            published=date.today()
        )
        self.booking = Bookings.objects.create(
            movie=self.movie,
            seat=self.seat,
            bookingDate=date.today()
        )

    def test_movie_serializer(self):
        serializer = MovieSerializer(self.movie)
        self.assertEqual(serializer.data['title'], "Interstellar")
        self.assertEqual(serializer.data['duration'], "02:28:00")

    def test_seat_serializer(self):
        serializer = SeatSerializer(self.seat)
        self.assertEqual(serializer.data['seatNumber'], "B2")
        self.assertTrue(serializer.data['bookingStatus'])

    def test_booking_serializer(self):
        serializer = BookingSerializer(self.booking)
        self.assertEqual(serializer.data['movie']['title'], "Interstellar")
        self.assertEqual(serializer.data['seat']['seatNumber'], "B2")