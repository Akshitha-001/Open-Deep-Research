# agents/writer.py
from core.llm import GeminiLLM

class WriterAgent:
    def __init__(self):
        self.llm = GeminiLLM()

    def write_summary(self, query: str, search_data: str):
        prompt = f"""
You are a research writer.

Topic: {query}

Here are the search results:
{search_data}

Write a clean, structured research summary with:
- Introduction
- Key insights
- Important definitions
- Real-world applications
- Conclusion
"""

        return self.llm.generate(prompt)
