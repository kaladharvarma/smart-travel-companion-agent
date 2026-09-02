import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def get_travel_advice(weather):

    prompt = f"""
You are Smart Travel Companion.

A traveller is visiting {weather['city']}.

Weather:
- Temperature: {weather['temperature']}°C
- Feels Like: {weather['feels_like']}°C
- Humidity: {weather['humidity']}%
- Condition: {weather['description']}
- Wind Speed: {weather['wind_speed']} km/h

Provide:
1. Weather Summary
2. Travel Recommendation
3. Clothing Suggestion
4. Whether to carry an umbrella
5. Any precautions

Keep the response short and friendly.
"""

    response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt,
    )

    #print(response)

    return response.text