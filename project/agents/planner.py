from typing import List


def plan(query: str) -> List[str]:
    # naive heuristics: split at common separators, and create 2-4 subtasks
    query = query.strip()
if not query:
    return ["General overview"]

# If user used question words, produce focused subtasks
subtasks = []
subtasks.append(f"Overview: {query}")
subtasks.append(f"Detailed explanations and definitions for: {query}")
subtasks.append(f"Recent developments and resources about: {query}")


# Keep unique and short
seen = set()
result = []
for s in subtasks:
if s not in seen:
seen.add(s)
result.append(s)
return result