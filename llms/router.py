from config.settings import PRIMARY_LLM

from llms.gemini_client import generate_response as gemini_response
from llms.groq_client import generate_response as groq_response


def generate_response(weather: str):

    if PRIMARY_LLM == "gemini":

        try:
            print("🤖 Using Gemini...\n")
            return gemini_response(weather)

        except Exception as e:

            print(f"Gemini failed: {e}")
            print("🔄 Falling back to Groq...\n")

            return groq_response(weather)

    elif PRIMARY_LLM == "groq":

        try:
            print("🤖 Using Groq...\n")
            return groq_response(weather)

        except Exception as e:

            print(f"Groq failed: {e}")
            print("🔄 Falling back to Gemini...\n")

            return gemini_response(weather)