import requests
from bs4 import BeautifulSoup


class BingImageScraper:
    def __init__(self):
        self.base_url = "https://www.bing.com/images/search"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }

    def search_images(self, query):
        params = {"q": query}

        response = requests.get(self.base_url, params=params, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        img = soup.find("img", {"class": "mimg"})
        if img and ("data-src" in img.attrs or "src" in img.attrs):
            return img["data-src"] if "data-src" in img.attrs else img["src"]
        else:
            return None


if __name__ == "__main__":
    query = "OLEO DE SOJA VILA VELHA 900ML - 900ML"

    bing_scraper = BingImageScraper()
    first_url = bing_scraper.search_images(query)

    if first_url:
        print("Primeira URL de imagem:", first_url)
    else:
        print("Nenhuma imagem encontrada.")
