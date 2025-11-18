# core/llm.py
import google.generativeai as genai
import os

class GeminiLLM:
    def __init__(self, model_name="gemini-1.5-flash"):
        api_key = os.getenv("AIzaSyBKFXW6HVUAwHlVtV3WT_gPOMPyKZR9QNQ")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(self, prompt: str):
        response = self.model.generate_content(prompt)
        return response.text
