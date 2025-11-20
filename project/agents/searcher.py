import os
from tavily import TavilyClient
from project.core.llm import GeminiLLM


class SearcherAgent:
    def __init__(self):
        tavily_api = os.getenv("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")
        if not tavily_api:
            raise ValueError("TAVILY_API_KEY missing! Set it in your environment.")

        self.search_client = TavilyClient(api_key=tavily_api)
        self.llm = GeminiLLM()

    def search(self, query: str):
        # Perform online search
        result = self.search_client.search(query=query, max_results=5)

        # Summarize using Gemini
        summary_prompt = f"""
        Summarize the following web search results in clear bullet points:

        {result}
        """

        summary = self.llm.generate(summary_prompt)
        return summary
