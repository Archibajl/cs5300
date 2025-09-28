from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    releaseDate = models.DateField()
    duration = models.DurationField()

class Seats(models.Model):
    seatNumber = models.IntegerField()
    bookingStatus = models.BooleanField(default=False)
    published = models.DateField()

class Bookings(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seats, on_delete=models.CASCADE)
    bookingDate = models.DateField()
