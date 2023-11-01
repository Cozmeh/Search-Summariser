import requests, random
from bs4 import BeautifulSoup
from transformers import pipeline


class summersearch:

    def __init__(self):
        self.result = {}
        self.links = []
        self.searchQuery = ""
        self.rawParagraph = ""
        self.url = "https://www.google.com/search?q="
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }

    def search(self, search_query,getLinks=3):
        execution_count = 0
        self.rawParagraph = ""
        self.searchQuery = search_query
        response = requests.get(self.url + self.searchQuery.replace(' ', '+'), headers=self.headers)
        if response.status_code == 200:
            self.links.clear()
            parsed = BeautifulSoup(response.text, "html.parser")
            search_results = parsed.find_all("div", class_="Gx5Zad fP1Qef xpd EtOod pkphOe")
            index = random.randint(0, 7)
            for result in search_results[index : index + getLinks]:
                link = result.find("a")["href"]
                l = link.split("/url?esrc=s&q=&rct=j&sa=U&url=")[1].split("&ved=")[0]
                self.links.append(l)
        else:
            raise Exception(f"Failed to retrieve search results. Status code: {response.status_code}")

        for link in self.links:
            response = requests.get(link, headers=self.headers)
            parsed_text = BeautifulSoup(response.text, "html.parser").find_all("p")
            for text in parsed_text:
                if text.get_text() != None and len(text.get_text()) > 250:
                    whitespace = text.get_text().count(" ")
                    if (whitespace / len(text.get_text())) * 100 < 20:
                        self.rawParagraph = self.rawParagraph + text.get_text().replace("\n", " ")
        
        if len(self.rawParagraph) < 300:
            if execution_count > 5:
                raise Exception("Failed to retrieve a paragraph of sufficient length.")
            else:
                self.search(search_query=self.searchQuery,getLinks=execution_count)
                execution_count += 1
                        
        return self.rawParagraph


    def summarise(self, Raw_Paragraph,model):
        if len(Raw_Paragraph) > 300:
            summarizer = pipeline("summarization",model=model)
            summary = summarizer(Raw_Paragraph, max_length=250, min_length=50,truncation=True)[0]["summary_text"]
            if self.links.count > 0 and self.searchQuery != "":
                self.result["search_query"] = self.searchQuery
                self.result["summary"] = summary
                self.result["reference"] = self.links[0]
                self.result["learn_more"] = self.links[1:]
            else:
                self.result["summary"] = summary
            return self.result
        else:          
            raise Exception("The provided paragraph is too short to summarise.")


