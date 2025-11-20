import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load .env file
load_dotenv()

class GeminiLLM:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError("GEMINI_API_KEY not found. Add it to .env file.")

        genai.configure(api_key=api_key)

        # Valid Gemini model
        self.model = genai.GenerativeModel("gemini-1.5-flash-latest")

    def generate(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text
