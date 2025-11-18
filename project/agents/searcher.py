from tavily import TavilyClient
import os

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search(tasks):
    outputs = {}
    for t in tasks:
        try:
            result = tavily.search(t)
            outputs[t] = result
        except Exception as e:
            outputs[t] = {"error": str(e)}
    return outputs
