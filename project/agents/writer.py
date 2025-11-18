from typing import Dict, Any, List




def write(plan: List[str], search_results: Dict[str, Any]) -> str:
"""Simple writer that combines plan and search results into a readable answer.


Replace with an LLM call for polished outputs later.
"""
lines: List[str] = []
lines.append("Research summary")
lines.append("===============\n")


for step in plan:
lines.append(f"TASK — {step}\n")
result = search_results.get(step)
if not result:
lines.append(" No results found.\n")
continue


rtype = result.get("type")
if rtype == "tavily":
items = result.get("items", [])
if not items:
lines.append(" (tavily returned no items)\n")
else:
# show top 3 titles/snippets (best-effort)
for i, it in enumerate(items[:3], 1):
# try to be tolerant about shape
title = it.get("title") if isinstance(it, dict) else str(it)
snippet = it.get("snippet") if isinstance(it, dict) else None
lines.append(f" {i}. {title}")
if snippet:
lines.append(f" snippet: {snippet}")
elif rtype == "local_llm":
items = result.get("items", [])
for i, it in enumerate(items, 1):
lines.append(f" {i}. {it}")
elif rtype == "error":
lines.append(f" Error: {result.get('error')}")
else:
lines.append(f" Unknown result type: {rtype}")
lines.append("")


lines.append("\nFinal notes: this is a draft — replace writer.write with an LLM-based composer for production.")
return "\n".join(lines)