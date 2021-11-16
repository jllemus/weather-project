# Rest framework imports
from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):

    city = serializers.CharField(
        max_length=225,
        allow_blank=True,
    )
    country = serializers.CharField(
        max_length=225,
        allow_blank=True,
    )

    def validate_city(self, value):
        """Validate if city contains only
        characters.

        Args:
            value (str): city value
        """
        if not value.isalpha():
            raise serializers.ValidationError(
                'City must contain only characters.'
            )
        return value

    def validate_country(self, value):
        """Validate country len > 2 and is lower
        case.

        Args:
            value (str): country value
        """
        if len(value) != 2:
            raise serializers.ValidationError(
                'Country code must contain only 2 characters.'
            )
        if value != value.lower():
            raise serializers.ValidationError(
                'Countr code must be lower case'
            )
        return value
