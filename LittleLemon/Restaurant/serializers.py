# Restaurant/serializers.py

from rest_framework import serializers
from .models import Reservation, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ["ID", "Title", "Price", "Inventory"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"
