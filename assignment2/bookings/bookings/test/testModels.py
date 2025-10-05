from django.test import TestCase
from bookings.models import Movies, Seats, Bookings
from datetime import date
from datetime import timedelta



class ModelTests(TestCase):
    def setUp(self):
        self.movie = Movies.objects.create(
            title="Inception",
            description="A mind-bending thriller",
            releaseDate=date(2010, 7, 16),
            duration=timedelta(minutes=148)
        )
        self.seat = Seats.objects.create(
            seatNumber="A1",
            bookingStatus=False,
            published=date.today()
        )
        self.booking = Bookings.objects.create(
            movie=self.movie,
            seat=self.seat,
            bookingDate=date.today()
        )

    def test_movie_fields(self):
        print(self.movie)
        print(self.movie.title)
        self.assertEqual(self.movie.title, "Inception")
        self.assertEqual(self.movie.duration, timedelta(minutes=148))

    def test_seat_fields(self):
        self.assertEqual(self.seat.seatNumber, "A1")
        self.assertTrue(self.seat.published)

    def test_booking_relationships(self):
        self.assertEqual(self.booking.movie.title, "Inception")
        self.assertEqual(self.booking.seat.seatNumber, "A1")