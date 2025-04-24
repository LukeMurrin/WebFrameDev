from django.test import TestCase
from users.models import User
from parcel_app.models import Parcel
from .models import Order

class OrderModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='customer', password='password', role='Customer')
        self.parcel = Parcel.objects.create(name='Test Parcel', weight=2.5, destination='New York')

    def test_order_creation(self):
        order = Order.objects.create(user=self.user, parcel=self.parcel)
        self.assertEqual(order.user.username, 'customer')
        self.assertEqual(order.parcel.name, 'Test Parcel')
        self.assertIsNotNone(order.order_date)
