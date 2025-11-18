# app.py
from agents.searcher import SearcherAgent
from agents.writer import WriterAgent

def main():
    query = input("Enter your research topic: ")

    searcher = SearcherAgent()
    writer = WriterAgent()

    print("\nSearching using Gemini...\n")
    search_results = searcher.search(query)

    print("Generating summary...\n")
    summary = writer.write_summary(query, search_results)

    print("\n===== FINAL SUMMARY =====\n")
    print(summary)

if __name__ == "__main__":
    main()
