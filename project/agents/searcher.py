# agents/searcher.py
from core.llm import GeminiLLM

class SearcherAgent:
    def __init__(self):
        self.llm = GeminiLLM()

    def search(self, query: str):
        prompt = f"""
You are a research search engine.
Return structured search results for the query:

Query: "{query}"

Return the results in this JSON-like list format:
[
  {{
    "title": "",
    "content": "",
    "source": ""
  }},
  ...
]

Ensure at least 5 high-quality results.
"""

        response = self.llm.generate(prompt)

        # We return raw LLM text because it's easier to parse later
        return response
