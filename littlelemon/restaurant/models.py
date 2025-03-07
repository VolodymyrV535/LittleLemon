from django.db import models
from django.utils import timezone  # Make sure this line is included


# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookings_date  = models.DateTimeField(default=timezone.now)
    

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
