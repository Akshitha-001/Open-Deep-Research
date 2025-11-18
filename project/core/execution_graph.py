from agents.planner import plan
from agents.searcher import search
from agents.writer import write
from core import memory
from typing import Any, Dict, List




class ResearchOrchestrator:
    def __init__(self):
        pass


def run(self, user_query: str) -> Dict[str, Any]:
    plan_steps: List[str] = plan(user_query)
    # store query and plan to memory
    memory.save("last_query", user_query)
    memory.save("last_plan", plan_steps)
    # 2. Search
    search_results = search(plan_steps)
    memory.save("last_search_results", search_results)
    # 3. Write
    final = write(plan_steps, search_results)
    memory.save("last_final", final)
    return {
        "plan": plan_steps,
        "search_results": search_results,
        "final": final,
}