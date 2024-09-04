# Restaurant/admin.py

from django.contrib import admin
from .models import Reservation, Menu

admin.site.register(Reservation)
admin.site.register(Menu)
