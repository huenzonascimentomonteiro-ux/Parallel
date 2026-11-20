import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=key)

def generate_content(text):

    prompt = f"""
    You are a social media content creator.

    Based on this personal progress report:
    {text}

    Create an short Instagram post.

    Keep the content authentic, never invent achievements, don't care about lowcase/upcase words.
    I have the images that i will use so don't care about anything that not is the text.
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text