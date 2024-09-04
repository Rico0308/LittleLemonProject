from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer


class MenuItemViewTest(APITestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.item2 = Menu.objects.create(Title="Cake", Price=150, Inventory=50)
        self.url = "/api/menu/"

    def test_get_all_items(self):
        response = self.client.get(self.url)
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
