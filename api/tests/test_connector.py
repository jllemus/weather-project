# Default imports
import re

# Django imports
from django.test import TestCase

# Api app imports
from api.connector import ApiConnector


class ApiRequestTestCase(TestCase):
    def setUp(self):
        self.api_conn = ApiConnector(city='Bogota', country='co')

    def test_validate_params(self):
        """Raises error when creating an empty object"""
        self.assertRaises(
            Exception, ApiConnector
        )

    def test_url_contains_params(self):
        """Params are in format &q=string,string"""
        url = self.api_conn.base_url
        match = re.findall(r'&q=[a-zA-Z]+\,[a-zA-Z]+', url)
        self.assertTrue(bool(match))

    def test_parse_response(self):
        """Returns dict with info parsed"""
        _, parsed_response = self.api_conn.get()
        self.assertTrue(len(parsed_response) > 1)

    def test_get(self):
        """Returns status 200."""
        response, parsed_response = self.api_conn.get()
        self.assertEqual(response.status_code, 200)
