# Restaurant/models.py

from django.db import models


class Reservation(models.Model):
    ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.PositiveIntegerField()
    BookingDate = models.DateTimeField()

    def __str__(self):
        return f"Reservation {self.id} for {self.name}"


class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    Inventory = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.Title} : {self.Price}"
