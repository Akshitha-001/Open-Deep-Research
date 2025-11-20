from project.core.llm import GeminiLLM

class PlannerAgent:
    def __init__(self):
        self.llm = GeminiLLM()

    def create_plan(self, topic: str):
        prompt = f"""
        Create a step-by-step research plan for the topic: {topic}.
        Include clear tasks and substeps.
        """
        return self.llm.generate(prompt)
