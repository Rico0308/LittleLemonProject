# Restaurant/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Crear el enrutador y registrar los ViewSets
router = DefaultRouter()
router.register(r"tables", views.BookingViewSet)  # Rutas para el ViewSet de reservas

# Configurar las URLs para las vistas basadas en clase y los ViewSets
urlpatterns = [
    path("menu/", views.MenuItemsView.as_view()),
    path("menu/<int:pk>/", views.SingleMenuItemView.as_view()),
    path("", include(router.urls)),  # Incluye las rutas del ViewSet
]
