from fastapi import FastAPI
from core.execution_graph import ResearchOrchestrator
import uvicorn


app = FastAPI(title="Research Agent API")


orchestrator = ResearchOrchestrator()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
async def ask(query: str):
    result = orchestrator.run(query)
    return {"query": query, "result": result}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)