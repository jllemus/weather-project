# Django imports
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Django rest framework imports
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Api app imports
from api.serializers import WeatherSerializer
from api.connector import ApiConnector


@method_decorator(cache_page(120), name='get')
class WeatherView(APIView):

    def get(self, request):
        filters = {
            key: value for key, value in request.query_params.items()
        }
        serializer = WeatherSerializer(data=filters)
        if serializer.is_valid():
            api_conn = ApiConnector(**serializer.validated_data)
            response = api_conn.get()
            return Response(
                data=response['response_data'],
                status=response['response_status'],
                content_type='application/json'
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
