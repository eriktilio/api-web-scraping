import requests


def obter_url_imagem_da_internet(nome):
    # Chave da API do Unsplash (substitua pela sua chave)
    chave_api_unsplash = "xXO_4p7ezf3RBG3wGaz3iUyQ8V-WBl5e9Z1HLg_mY0g"

    # Parâmetros da API do Unsplash
    parametros_api = {
        "query": nome,
        "client_id": chave_api_unsplash,
        "orientation": "landscape",  # Pode ajustar conforme necessário
    }

    # URL da API do Unsplash
    url_api_unsplash = "https://api.unsplash.com/photos/random"

    # Faz uma solicitação à API do Unsplash
    resposta = requests.get(url_api_unsplash, params=parametros_api)

    # Verifica se a solicitação foi bem-sucedida
    if resposta.status_code == 200:
        # Extrai a URL da imagem da resposta da API
        url_imagem = resposta.json()["urls"]["regular"]
        return url_imagem
    else:
        return "Erro ao obter a URL da imagem."


# Exemplo de uso
url_imagem_internet = obter_url_imagem_da_internet("TODDYNHO LEVINHO 200ML")

print("URL da imagem da internet:", url_imagem_internet)
