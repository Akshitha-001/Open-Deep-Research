from project.agents.planner import PlannerAgent
from project.agents.searcher import SearcherAgent
from project.agents.writer import WriterAgent
from project.core.memory import Memory


class ResearchOrchestrator:
    def __init__(self):
        self.memory = Memory()
        self.planner = PlannerAgent()
        self.searcher = SearcherAgent()
        self.writer = WriterAgent()

    def run(self, topic: str):
        plan = self.planner.create_plan(topic)
        self.memory.save("plan", plan)

        search_summary = self.searcher.search(topic)
        self.memory.save("search", search_summary)

        report = self.writer.write_report(plan, search_summary)
        self.memory.save("report", report)

        return {
            "plan": plan,
            "search_summary": search_summary,
            "report": report
        }
