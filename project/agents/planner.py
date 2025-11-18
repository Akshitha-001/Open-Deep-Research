def plan(query: str):
    query = query.strip()
    if not query:
        return ["General overview"]

    return [
        f"Overview: {query}",
        f"Important concepts about: {query}",
        f"Recent updates about: {query}",
    ]



#AIzaSyBKFXW6HVUAwHlVtV3WT_gPOMPyKZR9QNQ