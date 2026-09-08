import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_response(weather):

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

    response = client.chat.completions.create(
        model=os.getenv("MODEL_NAME"),
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content