from weather_tool import get_weather
from llm import get_travel_advice


def travel_companion(city):

    print("\nFetching weather...\n")

    weather = get_weather(city)

    print("Thinking...\n")

    advice = get_travel_advice(weather)

    print("=" * 60)
    print("SMART TRAVEL COMPANION")
    print("=" * 60)
    print(advice)