from django.test import TestCase, Client
from django.urls import reverse

class ParcelAppTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Parcel App!")

    def test_parcel_details_view(self):
        response = self.client.get(reverse('parcel_details'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is the Parcel Details page!")
