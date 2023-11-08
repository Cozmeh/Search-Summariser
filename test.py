from SummerSearch import summerSearch
# Create an instance
searcher = summerSearch()
print("Ready to search and summarize!")
# Perform a search
while True:
    search_query = input("Enter a search query: ")
    raw_paragraph = searcher.search(search_query=search_query,filter="fixed_index",filter_value=1)
    print("Generating summary...")
    # Summarize the content
    model = "t5-small"
    result = searcher.summarize(raw_paragraph, model)

    # Print the results
    print("\nSearch Query:", result["search_query"])
    print("\nSummary:", result["summary"])
    print("\nReference Link:", result["reference"])
    print("\nLearn More Links:", result["learn_more"])
    print("\nAdditional Links:", result["all_links"])
    