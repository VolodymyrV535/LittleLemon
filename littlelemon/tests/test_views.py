from django.test import TestCase
from restaurant.views import MenuItem
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.contrib.auth.models import User
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        
        # Authenticate the client
        self.client.login(username='testuser', password='testpass')
        
        MenuItem.objects.create(title='Pizza', price=10.99, inventory=5)
        MenuItem.objects.create(title='Pizza_Cheese', price=15.99, inventory=25)
        
    def test_getall(self):
        menus = MenuItem.objects.all()
        
        menus_serialized = MenuItemSerializer(menus, many=True)
        
        response = self.client.get('/restaurant/menu/')
        print(response)
        
        self.assertEqual(response.data, menus_serialized.data)
        self.assertEqual(response.status_code, 200)
