from project.core.llm import GeminiLLM

class WriterAgent:
    def __init__(self):
        self.llm = GeminiLLM()

    def write_report(self, outline: str, search_summary: str):
        prompt = f"""
        Write a detailed research report based on:

        OUTLINE:
        {outline}

        SEARCH SUMMARY:
        {search_summary}

        Provide a clear, well-structured explanation.
        """
        return self.llm.generate(prompt)
