import requests, random
from bs4 import BeautifulSoup
from transformers import pipeline

class summerSearch:

    def __init__(self):
        # Initialize instance variables
        self.result = {}  # A dictionary to store search results
        self.links = []  # A list to store extracted links from Google search
        self.searchQuery = ""  # The user's search query
        self.rawParagraph = ""  # A variable to store raw text paragraphs
        self.url = "https://www.google.com/search?q="  # The base Google search URL
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }  # User-Agent header to mimic a web browser

    def search(self, search_query, get_links=3):
        execution_count = 0  # A variable to track the number of execution attempts
        self.rawParagraph = ""  # Clear the rawParagraph for a new search
        self.searchQuery = search_query  # Set the search query for the instance

        # Send a request to Google search
        response = requests.get(self.url + self.searchQuery.replace(' ', '+'), headers=self.headers)
        
        if response.status_code == 200:
            self.links.clear()  # Clear the links list for a new search
            parsed = BeautifulSoup(response.text, "html.parser")
            # Find search result elements
            search_results = parsed.find_all("div", class_="Gx5Zad fP1Qef xpd EtOod pkphOe")
            index = random.randint(0, 7)  # Randomly select an index within the first 8 results

            # Extract search result links
            for result in search_results[index : index + get_links]:
                link = result.find("a")["href"]
                l = link.split("/url?esrc=s&q=&rct=j&sa=U&url=")[1].split("&ved=")[0]
                self.links.append(l)
        else:
            raise Exception(f"Failed to retrieve search results. Status code: {response.status_code}")

        # Extract paragraphs from the search result links
        if self.links:
            response = requests.get(self.links[0], headers=self.headers)
            parsed_text = BeautifulSoup(response.text, "html.parser").find_all("p")
            for text in parsed_text:
                if text.get_text() != None and len(text.get_text()) > 250:
                    # Check if the text has enough content based on length and whitespace ratio
                    whitespace = text.get_text().count(" ")
                    if (whitespace / len(text.get_text())) * 100 < 20:
                        self.rawParagraph = self.rawParagraph + text.get_text().replace("\n", " ")
        else:
            raise Exception("Failed to retrieve links.")
        # Retry the search if the paragraph is too short
        if len(self.rawParagraph) < 300:
            if execution_count > 5:
                raise Exception("Failed to retrieve a paragraph of sufficient length.")
            else:
                # Recursively call the search method with the same query but increment the execution count
                self.search(search_query=self.searchQuery, get_links=execution_count)
                execution_count += 1

        return self.rawParagraph

    def summarize(self, raw_paragraph, model):
        if len(raw_paragraph) > 300:
            summarizer = pipeline("summarization", model=model)
            # Use a summarization model to generate a summary
            summary = summarizer(raw_paragraph, max_length=250, min_length=50, truncation=True)[0]["summary_text"]

            if self.links:
                self.result["search_query"] = self.searchQuery
                self.result["summary"] = summary
                self.result["reference"] = self.links[0]
                self.result["learn_more"] = self.links[1:]
            else:
                self.result["summary"] = summary
            return self.result
        else:
            raise Exception("The provided paragraph is too short to summarize.")

