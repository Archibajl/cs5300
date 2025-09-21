from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    releaseDate = models.DateField()
    duration = models.DurationField()

class Seat(models.Model):
    seatNumber = models.IntegerField()
    bookingStatus = models.Boolean()
    published = models.DateField()

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForignKey(Seat, on_delete=models.CASCADE)
    bookingDate = models.DateField()
