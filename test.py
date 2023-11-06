from SummerSearch import summerSearch
# Create an instance
searcher = summerSearch()
print("Ready to search and summarize!")
# Perform a search
while True:
    search_query = input("Enter a search query: ")
    raw_paragraph = searcher.search(search_query=search_query,accuracy=1)
    print("Generating summary...")
    # Summarize the content
    model = "t5-small"
    result = searcher.summarize(raw_paragraph, model)

    # Print the results
    print("Search Query:", result["search_query"])
    print("Summary:", result["summary"])
    print("Reference Link:", result["reference"])
    print("Learn More Links:", result["learn_more"])
    