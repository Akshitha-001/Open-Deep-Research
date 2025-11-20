from project.core.llm import GeminiLLM

class SearcherAgent:
    def __init__(self):
        self.llm = GeminiLLM()

    def search(self, query: str) -> str:
        prompt = f"""
        Act as a research search agent.

        Your job:
        - Search the web using your internal knowledge
        - Extract the top facts
        - Return a short summary of key findings

        Query: {query}

        Provide accurate and reliable information.
        """

        return self.llm.generate(prompt)
