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
            "num": 1,  # Limita a busca a 1 resultado (imagem)
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


# Exemplo de uso da classe
buscador = SearchImageGoogle()

# Substitua "nome_do_produto" pelo nome real do produto que você está procurando
nome_do_produto = "ARROZ SUPERUM 1KG"

# Chama o método para obter a URL da imagem do produto
url_imagem_produto = buscador.get_url_image(nome_do_produto)

# Exibe a URL da imagem (ou None se houver um erro)
print("URL da imagem do produto:", url_imagem_produto)
