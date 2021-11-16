# Django imports
from django.urls import path

# Weather app imports
from api.views import WeatherView

urlpatterns = [
    path('', WeatherView.as_view(), name='weather-api'),
]
