import requests

from travel_agent.tools.constants import GEOCODE_API, WEATHER_API


def get_weather(city: str) -> str:
    """
    Returns the current weather for a given city.

    Args:
        city: Name of the city (e.g., Tokyo, switzerland, London).

    Returns:
        A human-readable weather summary.
    """

    try:
        geo_response = requests.get(
            GEOCODE_API,
            params={
                "name": city,
                "count": 1,
            },
            timeout=10,
        )
        geo_response.raise_for_status()

        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return f"Weather information is unavailable for '{city}'."

        location = geo_data["results"][0]

        weather_response = requests.get(
            WEATHER_API,
            params={
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": (
                    "temperature_2m,apparent_temperature,wind_speed_10m,weather_code"
                ),
            },
            timeout=10,
        )
        weather_response.raise_for_status()

        weather_data = weather_response.json()

        current = weather_data.get("current")

        if not current:
            return f"Weather information is unavailable for '{city}'."

        return (
            f"Location: {location['name']}\n"
            f"Temperature: {current['temperature_2m']}°C\n"
            f"Feels Like: {current['apparent_temperature']}°C\n"
            f"Wind Speed: {current['wind_speed_10m']} km/h\n"
            f"Weather Code: {current['weather_code']}"
        )

    except requests.RequestException:
        return f"Unable to fetch weather information for '{city}'."
