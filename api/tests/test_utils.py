# Default imports
import re

# Django imports
from django.test import TestCase

# Api app imports
from api.connector import ApiConnector
from api.utils import (
    get_wind_information, get_cloudiness,
    get_humidity, get_sunrise, get_pressure,
    get_temperatures, get_coordinates
)


class UtilsTestCase(TestCase):

    def setUp(self):
        response, _ = ApiConnector(
            city='Bogota', country='co'
        ).get()
        self.response = response.json()

    def test_get_temperatures(self):
        """Celsius in fahrenheint are in temperature json"""
        temps = get_temperatures(self.response.get('main'))
        self.assertIn('celsius', temps)
        self.assertIn('fahrenheit', temps)

    def test_get_wind_information(self):
        """Returns wind information as string"""
        wind_info = get_wind_information(self.response.get('wind'))
        self.assertTrue(isinstance(wind_info, str))

    def test_get_cloudiness(self):
        """Check weather info is returned capitalized"""
        cloud = get_cloudiness(self.response.get('weather'))
        self.assertTrue(isinstance(cloud, str))
        self.assertTrue(cloud[0].isupper())

    def test_get_humidity(self):
        """Check humidity is returned with percentage symbol"""
        humidity = get_humidity(self.response.get('main'))
        self.assertTrue(isinstance(humidity, str))
        self.assertIn('%', humidity)

    def test_get_sunrise(self):
        """Check datetime is returned as str and only time
        is returned"""
        time = get_sunrise(self.response.get('sys').get('sunrise'))
        match = re.findall(r'[0-9]{2}:[0-9]{2}', time)
        self.assertTrue(isinstance(time, str))
        self.assertTrue(bool(match))

    def test_get_coordinates(self):
        """Check coordinates are returned as a str array"""
        coord = get_coordinates(self.response.get('coord'))
        match = re.match(r'\[[0-9.,\- ]*\]', coord)
        self.assertTrue(isinstance(coord, str))
        self.assertTrue(bool(match))

    def test_get_pressure(self):
        """Check pressure is returned as hpa"""
        press = get_pressure(self.response.get('main'))
        self.assertTrue(isinstance(press, str))
        self.assertIn('hpa', press)
