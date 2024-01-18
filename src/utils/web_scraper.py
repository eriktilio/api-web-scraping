import re

import requests
from bs4 import BeautifulSoup

from constants import BASE_URL


class WebScraper:
    def __init__(self, url):
        self.url = BASE_URL + url

    def __scrape_data(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        cards = soup.find_all("div", class_="card small p hoverable")

        result = []
        for card in cards:
            title = card.find("span").text.strip()
            price = re.sub(r"R\$ ", "", card.find("p").text.strip())
            local = card.find("p", class_="truncate tooltipped padding10").text.strip()
            last_update = card.find("p", class_="tb-valor-10").text.strip()
            address = card.find(
                "span", class_="truncate grey-text text-darken-4 tb-valor-10 tooltipped"
            ).text.strip()

            data = {
                "title": title,
                "price": price,
                "local": local,
                "last_update": last_update,
                "address": address,
            }
            if local and price and title:
                result.append(data)

        return result

    def get_data(self):
        data = self.__scrape_data()
        return data
