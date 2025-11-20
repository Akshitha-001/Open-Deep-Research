import os
import google.generativeai as genai

class GeminiLLM:
    def __init__(self, model="gemini-1.5-flash-latest"):
        api_key = os.getenv("AIzaSyBKFXW6HVUAwHlVtV3WT_gPOMPyKZR9QNQ")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found. Set it in your environment.")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)

    def generate(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text
