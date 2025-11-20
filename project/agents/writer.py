from project.core.llm import GeminiLLM

class WriterAgent:
    def __init__(self):
        self.llm = GeminiLLM()

    def write_report(self, topic: str, search_data: str) -> str:
        prompt = f"""
        You are a senior technical writer.

        Topic: {topic}

        Research Summary (from Search Agent):
        {search_data}

        Write a full structured research report including:
        - Introduction
        - Detailed Explanation
        - Key Concepts
        - Technical Depth
        - Practical Applications
        - Advantages
        - Limitations
        - Conclusion

        Use simple and clear language.
        """

        return self.llm.generate(prompt)
