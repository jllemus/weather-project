# Default imports
import json
import requests
import datetime

# Django settings imports
from django.conf import settings

# Django rest framework imports
from rest_framework import status

# Api app imports
from api.utils import (
    get_cloudiness, get_humidity, get_pressure,
    get_coordinates, get_sunrise, get_temperatures,
    get_wind_information,
)


class ApiConnector():
    """Class created to define http methods
    to default API.
    """
    API_KEY = getattr(settings, 'API_KEY', None)
    API_URL = getattr(settings, 'API_URL', None)

    def __init__(self, **kwargs):
        """Constructor"""
        self.params = {**kwargs}
        self.base_url = f'{self.API_URL}?appid={self.API_KEY}'
        self._validate_params()

    def _validate_params(self):
        """Validates params passed to class.

        Raises:
            Exception: city value must be passed
            Exception: country value must be passed
        """
        if not self.params.get('city') or not self.params.get('country'):
            raise Exception('City and country value are required')

        self.base_url += f'&q={self.params["city"]},{self.params["country"]}'

    def _parse_response(self, response):
        response = response.json()
        parsed_response = {
            'location_name': '{},{}'.format(
                self.params['city'].capitalize(),
                self.params['country'].upper()
            ),
            'temperatures': get_temperatures(response.get('main')),
            'wind': get_wind_information(response.get('wind')),
            'cloudiness': get_cloudiness(response.get('weather')),
            'pressure': get_pressure(response.get('main')),
            'humidity': get_humidity(response.get('main')),
            'sunrise': get_sunrise(response.get('sys').get('sunrise')),
            'sunset': get_sunrise(response.get('sys').get('sunset')),
            'geo_coordinates': get_coordinates(response.get('coord')),
            'requested_time': datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S UTC'
            )
        }
        return parsed_response

    def get(self):
        response = requests.get(self.base_url)
        parsed_response = {
            'response_status': response.status_code
        }
        if response.status_code != status.HTTP_200_OK:
            parsed_response['response_data'] = {
                'message': response.json().get('message')
            }
            return parsed_response
        parsed_response['response_data'] = self._parse_response(response)
        return parsed_response
