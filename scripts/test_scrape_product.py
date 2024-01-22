import json

import requests
from bs4 import BeautifulSoup


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def scrape_data(self):
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

    def get_pagination(self):
        pagination = self.soup.find("ul", class_="pagination")
        li_list = pagination.find_all("li")

        page_numbers = []

        for li in li_list:
            a = li.find("a")
            if a is not None and a.text.isdigit():
                page_numbers.append(int(a.text))

        if page_numbers:
            max_page = max(page_numbers)
        else:
            max_page = 0

        return {"total_pages": max_page, "pages": page_numbers}

    def data_to_json(self):
        data = self.get_pagination()
        return json.dumps(data, ensure_ascii=False, indent=2)


# Exemplo de uso
URL = "https://buscapreco.sefaz.am.gov.br/item/grupo/page/14?termoCdGtin=&descricaoProd=gasolina&action="
scraper = WebScraper(URL)
json_result = scraper.data_to_json()
print(json_result)
