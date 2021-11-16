# Api app imports
from api.serializers import WeatherSerializer

# Django imports
from django.test import TestCase


class WeatherSerializerTestCase(TestCase):

    def setUp(self):
        self.serializer = WeatherSerializer

    def test_serializer_accepts_default_fields(self):
        """Check serializer accepts default fields"""
        data = {
            'city': 'Bogota',
            'country': 'Colombia'
        }
        serializer = self.serializer(data=data)
        if serializer.is_valid():
            data = self.serializer.data
            self.assertEqual(set(data.keys()), set(['city', 'country']))

    def test_validate_city(self):
        """Check serializer only accepts text characters in city
        field."""
        data = {
            'city': 'Bogota2',
            'country': 'co'
        }
        serializer = self.serializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_validate_country(self):
        """Check serializer only accepts country code as a 2 character
        lowercase."""
        data = {
            'city': 'Bogota',
            'country': 'Co'
        }
        serializer = self.serializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_validate_fields_required(self):
        """Check city and country are required fields."""
        data = {}
        serializer = self.serializer(data=data)
        self.assertFalse(serializer.is_valid())
