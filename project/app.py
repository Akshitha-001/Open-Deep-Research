from project.searcher import SearcherAgent
from project.writer import WriterAgent

def main():
    print("=== Open Deep Research System (Gemini Version) ===")

    topic = input("Enter your research topic: ")

    searcher = SearcherAgent()
    writer = WriterAgent()

    print("\nSearching information...\n")
    search_results = searcher.search(topic)

    print("Generating detailed research report...\n")
    report = writer.write_report(topic, search_results)

    print("\n===== FINAL RESEARCH REPORT =====\n")
    print(report)

if __name__ == "__main__":
    main()
