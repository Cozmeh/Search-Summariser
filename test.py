from SummerSearch import summerSearch
# Create an instance
searcher = summerSearch()
print("Ready to search and summarize!")
# Perform a search
while True:
    search_query = input("Enter a search query: ")
    raw_paragraph = searcher.search(search_query=search_query,filter="fixed_index",filter_value=1)
    print("Generating summary...")
    print(raw_paragraph)
    # Summarize the content
    model = "t5-small"
    result = searcher.summarize(raw_paragraph, model)

    # Print the results
    print("\nSearch Query:", result["search_query"])
    print("\nSummary:", result["summary"])
    print("\nReference Link:", result["reference"])
    print("\nLearn More Links:", result["learn_more"])
    print("\nAdditional Links:", result["all_links"])




# l = link.split('/url?q=')[1].split('&sa=U&')[0]  - should be used when headers are not gived to requests 

# # with open('withheader.html', 'w', encoding='utf-8') as f:
# #     f.write(response.text)


# # from transformers import TFT5ForConditionalGeneration, T5Tokenizer
# # # model init and tokenizer (t5 smaller model)
# # model_name = "t5-small"
# # model = TFT5ForConditionalGeneration.from_pretrained(model_name)
# # tokenizer = T5Tokenizer.from_pretrained(model_name)

# from transformers import BartForConditionalGeneration, BartTokenizer
# # model init and tokenizer (bart large cnn model)
# model_name = "facebook/bart-large-cnn"
# model = BartForConditionalGeneration.from_pretrained(model_name)
# tokenizer = BartTokenizer.from_pretrained(model_name)

# inputs = tokenizer.encode(paragraph, return_tensors="pt", max_length=1024, truncation=True)
# summary_ids = model.generate(inputs, max_length=200, min_length=40, length_penalty=1.0, num_beams=4, early_stopping=True)
# summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)


# kabita-choudhary/finetuned-bart-for-conversation-summary - for conversation summary 
# facebook/bart-large-cnn - for general and more proper summary
# t5-small - for general and basic summary