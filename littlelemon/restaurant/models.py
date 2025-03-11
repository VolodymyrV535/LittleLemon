from django.db import models
from django.utils import timezone  # Make sure this line is included


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    bookings_date  = models.DateTimeField(default=timezone.now)
    

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price =  models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
<<<<<<< HEAD
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
    
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'
=======
>>>>>>> parent of 20e8cb6 (added drf and djoser based authentication to api)
