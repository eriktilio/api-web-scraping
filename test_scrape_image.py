import json

import requests
from bs4 import BeautifulSoup


class GasolinaComumScraper:
    def __init__(self, url):
        self.url = url

    def scrape_data(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        cards = soup.find_all("div", class_="card small p hoverable")

        result = []
        for card in cards:
            title = card.find("span").text.strip()
            price = card.find("p").text.strip()
            local = card.find("p", class_="truncate tooltipped padding10").text.strip()
            last_update = card.find("p", class_="tb-valor-10").text.strip()
            address = card.find(
                "span", class_="truncate grey-text text-darken-4 tb-valor-10 tooltipped"
            ).text.strip()

            data = {
                "Titulo": title,
                "Preço": price,
                "Local": local,
                "Atualizado": last_update,
                "Endereço": address,
            }
            result.append(data)

        return result

    def data_to_json(self):
        data = self.scrape_data()
        return json.dumps(data, ensure_ascii=False, indent=2)


# Exemplo de uso
URL = "https://buscapreco.sefaz.am.gov.br/item/grupo/page/1?termoCdGtin=&descricaoProd=gasolina+comum&action="
scraper = GasolinaComumScraper(URL)
json_result = scraper.data_to_json()
print(json_result)
