from project.core.execution_graph import ResearchOrchestrator

def main():
    topic = input("Enter research topic: ")

    orchestrator = ResearchOrchestrator()
    result = orchestrator.run(topic)

    print("\n===== RESEARCH PLAN =====")
    print(result["plan"])

    print("\n===== SEARCH SUMMARY =====")
    print(result["search_summary"])

    print("\n===== FINAL REPORT =====")
    print(result["report"])


if __name__ == "__main__":
    main()
