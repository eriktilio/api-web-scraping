import requests

from constants import KEY_API_GOOGLE, KEY_CX_ID_GOOGLE


class SearchImageGoogle:
    def __init__(self):
        self.url_api = "https://www.googleapis.com/customsearch/v1"
        self.key_api = KEY_API_GOOGLE
        self.cx_id = KEY_CX_ID_GOOGLE

    def get_url_image(self, item_name):
        # Parâmetros da consulta
        params = {
            "q": item_name,
            "key": self.key_api,
            "cx": self.cx_id,
            "searchType": "image",
            "fileType": "png",
            "num": 1,
        }

        try:
            # Faz a requisição à API
            response = requests.get(self.url_api, params=params)
            response.raise_for_status()  # Verifica se há erros na resposta

            # Obtém a URL da imagem do primeiro resultado
            result = response.json()["items"][0]
            url_image = result["link"]

            return url_image

        except (requests.exceptions.RequestException, KeyError, IndexError) as e:
            print(f"Erro: {e}")
            return None
