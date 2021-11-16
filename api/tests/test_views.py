# Django imports
from django.urls import reverse
from django.test import TestCase

# Django rest framework
from rest_framework import status
from rest_framework.test import APIClient


class WeatherViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('weather-api')

    def test_get(self):
        """Test GET method responds HTTP_200_OK"""
        client = APIClient()
        response = client.get(
            self.url,
            {
                'city': 'Bogota',
                'country': 'co'
            }
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
