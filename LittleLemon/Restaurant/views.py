# Restaurant/views.py

from rest_framework import generics, viewsets
from .models import Menu, Reservation
from .serializers import MenuSerializer, BookingSerializer


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = BookingSerializer
