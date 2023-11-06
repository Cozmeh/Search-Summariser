import requests, random
from bs4 import BeautifulSoup
from transformers import pipeline

class summerSearch:

    # Constructor
    def __init__(self):
        self.output = {}  
        self.results = []  # A list to store extracted links
        self.search_query = ""  # The user's search query
        self.raw_paragraph = ""  # A variable to store raw text paragraphs
        self.url = "https://www.google.com/search?q="  # The base search URL
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }  # User-Agent header to mimic a web browser

    # Gets the links for the search query
    def __get_links(self):
        response = requests.get(self.url + self.search_query.replace(' ', '+'), headers=self.headers)
        if response.status_code == 200  :
            self.results.clear()  # Clear the links list for a new search
            parsed = BeautifulSoup(response.text, "html.parser")
            # Find search result elements
            search_results = parsed.find_all("div", class_="Gx5Zad fP1Qef xpd EtOod pkphOe")
            # Extract search result links
            for result in search_results:
                link = result.find("a")["href"].split("/url?esrc=s&q=&rct=j&sa=U&url=")[1].split("&ved=")[0]
                self.results.append(link)
        else:
            raise Exception(f"Failed to retrieve search results. \nStatus code: {response.status_code}")

    # Extracts the raw text from the links
    def __extract(self,accuracy):
        index = random.randint(0, accuracy)
        source = self.results[index:index+1]
        if self.results:
            response = requests.get(url=source[0], headers=self.headers)
            parsed_text = BeautifulSoup(response.text, "html.parser").find_all("p")
            self.results[0] = source[0]
            for text in parsed_text:
                if text.get_text() != None and len(text.get_text()) > 250:
                    # Check if the text has enough content based on length and whitespace ratio
                    whitespace = text.get_text().count(" ")
                    if (whitespace / len(text.get_text())) * 100 < 20:
                        self.raw_paragraph = self.raw_paragraph + text.get_text().replace("\n", " ")
        else:
            raise Exception("Search results not found!")

    # Performs a search and returns the raw paragraph
    def search(self, search_query, accuracy=3): 
        if search_query == "":
            raise Exception(f"Search query not found! \nProvided search_query:{search_query}")
        if accuracy not in range(1,6):
            raise Exception(f"Accuracy must be between 1 and 5. \nProvided accuracy:{accuracy}")
        
        self.raw_paragraph = ""  
        self.search_query = search_query  
        self.__get_links() 
        self.__extract(accuracy)
        # If the raw_paragraph is empty or is less than 300 characters, try again with a lower accuracy(+1)
        if self.raw_paragraph == "" and len(self.raw_paragraph) < 300:
            self.__extract(accuracy+1)

        return self.raw_paragraph

    # Summarizes the raw paragraph
    def summarize(self, raw_paragraph, model):
        if len(raw_paragraph) > 300:
            summarizer = pipeline("summarization", model=model)
            # Use a summarization model to generate a summary
            summary = summarizer(raw_paragraph, truncation=True)[0]["summary_text"]
            if self.results:
                self.output["search_query"] = self.search_query
                self.output["summary"] = summary
                self.output["reference"] = self.results[0]
                self.output["learn_more"] = random.choices(self.results, k=2)
            else:
                self.output["summary"] = summary
            return self.output
        else:
            raise Exception("Raw paragraph is too short to summarize.")

