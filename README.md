# Summer Search

**summer-search** is a Python package that provides a simple interface for searching the web, extracting relevant content, and generating a summary based on the extracted information. The package leverages popular libraries such as `requests`, `BeautifulSoup`, and `transformers` to achieve its functionality.

## Installation

You can install the package using pip:

```cmd
pip install summer-search
```


### Requirements:

- **bs4 (Beautiful Soup 4):**
- **requests:**
- **transformers:**
- **sentencepiece:**
- **tensorflow:**
- **torch:**
> checkout the [requirements.txt](https://github.com/Cozmeh/SummerSearch/blob/main/requirements.txt)
  ```bash
   pip install -r requirements.txt
  ```
  

Make sure to install these dependencies before using the `summer-search` package to ensure all the required libraries are available.

## Usage

```python
from SummerSearch import summerSearch

# Create an instance
searcher = summerSearch()
print("Ready to search and summarize!")

# Perform a search
while True:

    # query to search 
    search_query = input("Enter a search query: ")
    raw_paragraph = searcher.search(search_query=search_query,filter="fixed_index",filter_value=1)
    print("Generating summary...")

    #specifying the model
    model = "t5-small"

    #summerization
    result = searcher.summarize(raw_paragraph, model)

    # Print the results
    print("\nSearch Query:", result["search_query"])
    print("\nSummary:", result["summary"])
    print("\nReference Link:", result["reference"])
    print("\nLearn More Links:", result["learn_more"])
    print("\nAdditional Links:", result["all_links"])
```

## Documentation

- `summerSearch` Class

#### Methods

- `search(search_query, filter="accuracy", filter_value=2)`: Performs a search and returns the raw paragraph.
  - `search_query`: The user's search query.
  - `filter`: Filtering option ("accuracy" or "fixed_index").
  - `filter_value`: Value based on the selected filter (default is 2).

- `summarize(raw_paragraph, model)`: Summarizes the raw paragraph using a specified model.
  - `raw_paragraph`: The raw text to be summarized.
  - `model`: The summarization model to use.
 

## Summarization Models

The `summerSearch` class supports the following summarization models:

- **t5-small**: A small variant of the T5 (Text-to-Text Transfer Transformer) model for general and basic summaries.

- **facebook/bart-large-cnn**: The BART (BART: Denoising Sequence-to-Sequence Pre-training) model, specifically the large CNN variant, for general and more proper summaries.

- **kabita-choudhary/finetuned-bart-for-conversation-summary**: A fine-tuned BART model for conversation summaries.


Feel free to choose the model that best fits your requirements and experiment with different models to observe variations in summarization results.

## Notes
Feel free to explore and experiment with the package
- You can always contribute to the package!
- The package uses a combination of web scraping and summarization techniques to provide relevant information based on the user's search query.
- The `filter` and `filter_value` parameters in the `search` method allow users to customize the search process based on accuracy or a fixed index.
- The `summarize` method utilizes the Hugging Face Transformers library for text summarization.
