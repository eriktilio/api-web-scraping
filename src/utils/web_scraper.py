import re

import requests
from bs4 import BeautifulSoup

from constants import BASE_URL


class WebScraper:
    def __init__(self, url):
        self.url = BASE_URL + url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def __scrape_data(self):
        cards = self.soup.find_all("div", class_="card small p hoverable")

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
                "url_image": None,
                "last_update": last_update,
                "address": address,
            }
            if local and price and title:
                result.append(data)

        return result

    def get_data(self):
        data = self.__scrape_data()
        return data

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
