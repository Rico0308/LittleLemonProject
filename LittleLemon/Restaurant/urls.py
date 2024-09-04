# Restaurant/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

# Crear el enrutador y registrar los ViewSets
router = DefaultRouter()
router.register(r"tables", views.BookingViewSet)  # Rutas para el ViewSet de reservas

# Configurar las URLs para las vistas basadas en clase y los ViewSets
urlpatterns = [
    path("menu-items/", views.MenuItemsView.as_view()),
    path("menu-items/<int:pk>/", views.SingleMenuItemView.as_view()),
    path("", include(router.urls)),
    path("message/", views.msg),
    path("api-token-auth/", obtain_auth_token),
]
