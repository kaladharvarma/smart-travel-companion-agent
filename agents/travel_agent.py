from tools.weather_tool import get_weather
from llms.router import generate_response


def travel_companion(city: str):

    print("\nFetching weather...\n")

    weather = get_weather(city)

    print("Thinking...\n")

    advice = generate_response(weather)

    print("=" * 60)
    print("SMART TRAVEL COMPANION")
    print("=" * 60)
    print(advice)