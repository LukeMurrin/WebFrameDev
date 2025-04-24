from django.test import TestCase
from .models import User
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()  # Ensure the custom User model is used

class UserModelTests(TestCase):

    def setUp(self):
        User.objects.create(username='customer1', role='Customer')
        User.objects.create(username='delivery1', role='Delivery Personnel')
        User.objects.create(username='warehouse1', role='Warehouse Staff')

    def test_user_creation(self):
        customer = User.objects.get(username='customer1')
        delivery_person = User.objects.get(username='delivery1')
        warehouse_staff = User.objects.get(username='warehouse1')

        self.assertEqual(customer.role, 'Customer')
        self.assertEqual(delivery_person.role, 'Delivery Personnel')
        self.assertEqual(warehouse_staff.role, 'Warehouse Staff')

    def test_user_str(self):
        user = User.objects.get(username='customer1')
        self.assertEqual(str(user), 'customer1')  # Assuming __str__ method returns username

    def test_user_role(self):
        user = User.objects.get(username='delivery1')
        self.assertEqual(user.role, 'Delivery Personnel')

class RoleBasedAccessTests(TestCase):
    def setUp(self):
        self.customer = User.objects.create_user(username='customer', password='password', role='Customer')
        self.admin = User.objects.create_user(username='admin', password='password', role='Admin')

    def test_customer_access_profile(self):
        login_successful = self.client.login(username='customer', password='password')  # Log in as customer
        self.assertTrue(login_successful)  # Ensure login is successful

        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)  # Ensure the profile page is accessible
        self.assertContains(response, "Username: customer")

    def test_admin_access_profile(self):
        login_successful = self.client.login(username='admin', password='password')  # Log in as admin
        self.assertTrue(login_successful)  # Ensure login is successful

        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)  # Ensure the profile page is accessible
        self.assertContains(response, "Username: admin")

    def test_redirect_for_unauthenticated_user(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # Ensure unauthenticated users are redirected
        self.assertIn('/users/login/', response.url)  # Check the redirection URL