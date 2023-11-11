from django.db import models
from datetime import datetime
# Create your models here.

class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, db_index=True)
    inventory = models.SmallIntegerField()


class Booking(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    no_of_guests = models.SmallIntegerField()
    BookingDate = models.DateTimeField()