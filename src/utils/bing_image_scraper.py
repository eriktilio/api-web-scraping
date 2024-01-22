import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


class BingImageScraper:
    def __init__(self):
        self.base_url = "https://www.bing.com/images/search"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        }

    def get_url_image(self, query):
        try:
            params = {"q": f"{query}"}
            response = requests.get(self.base_url, params=params, headers=self.headers)
            response.raise_for_status()

            # Verificar se a resposta contém conteúdo
            if not response.text:
                return None

            # Utilizando o parser lxml
            soup = BeautifulSoup(response.text, "lxml")

            # Encontrar a primeira imagem diretamente
            img = soup.find("img", {"class": "mimg"}) or soup.find(
                "img", {"class": "mimg vimgld"}
            )

            if img and "src" in img.attrs:
                return img["src"]
            else:
                return None

        except RequestException as e:
            print(f"Erro ao fazer a solicitação: {e}")
            return None
