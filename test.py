import requests
from bs4 import BeautifulSoup

URL = "https://buscapreco.sefaz.am.gov.br/home"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
title = soup.title.text.strip()
content = soup.find("div")


print(title, content)
