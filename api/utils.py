# Default imports
import datetime

# Project utilities
from weather_app.utils import WIND_RANGES, CARDINAL_DIRECTION


def get_temperatures(main):
    """Gets temperature from response and returns
    a dict with celsius and fahrenheint scales.capitalize()

    Args:
        main (dict): main attribute in json response

    Returns:
        dict: dictionary containing temperature in celsius
        and fahrenheit
    """
    temperatures = {
        'celsius': main.get('temp') - 273.15,
        'fahrenheit': (main.get('temp') - 273.15) * 9/5 + 32
    }
    return temperatures


def get_wind_information(wind):
    """This method gets wind dictionary with
    wind information and returns a list with a wind
    description

    Args:
        wind (dict): wind attribute coming from response

    Returns:
        str: string wind description
    """
    wind_ranges = WIND_RANGES
    cardinal_directions = CARDINAL_DIRECTION

    wind_info = []
    for desc, wind_range in wind_ranges.items():
        if wind_range[0] <= wind.get('speed') < wind_range[1]:
            wind_info.append(desc)
    if not wind_info:
        wind_info.append('Near Gale')

    wind_info.append(
        f'{wind.get("speed")}{"m/s"}'
    )

    for desc, direction in cardinal_directions.items():
        if direction[0] <= wind.get('deg') < direction[1]:
            wind_info.append(desc)
    return ', '.join(wind_info)


def get_cloudiness(weather):
    """Gets cloudines info coming from request and
    returns the cloud description

    Args:
        weather (dict): weather attribute coming from request.

    Returns:
        str: cloud string description
    """
    return weather[0].get('description').capitalize()


def get_pressure(main):
    """This method gets main attribute in
    response and returns pressure as a string.

    Args:
        main (dict): main attribute coming from response

    Returns:
        str: string pressure
    """
    return f'{main.get("pressure")} hpa'


def get_humidity(main):
    """This method gets main attribute in
    response and returns humidity as a string.

    Args:
        main (dict): main attribute coming from response

    Returns:
        str: string humidity
    """
    return f'{main.get("humidity")}%'


def get_sunrise(unix_time):
    """This method gets unix_times in response
    and returns it as as a string datetime.

    Args:
        unix_time (dict): unix time

    Returns:
        str: string time
    """
    return datetime.datetime.utcfromtimestamp(
        int(unix_time)
    ).strftime('%H:%M UTC')


def get_coordinates(coord):
    """This method gets coord dict in response
    and returns it as as a string list.

    Args:
        coord (dict): coord attribute coming in response

    Returns:
        str: string coordinates
    """
    return f'[{coord.get("lon")}, {coord.get("lat")}]'
