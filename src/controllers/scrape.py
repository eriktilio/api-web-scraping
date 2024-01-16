import requests
from bs4 import BeautifulSoup
from fastapi import Depends, HTTPException

from src.models import schemes as schemas


# Função para resolver CAPTCHA usando pytesseract
def resolve_captcha(image_url):
    # Faz o download da imagem do CAPTCHA
    response = requests.get(image_url, stream=True)
    response.raise_for_status()

    # Abre a imagem usando o PIL (Python Imaging Library)
    with Image.open(response.raw) as img:
        # Usa pytesseract para extrair o texto do CAPTCHA
        captcha_text = pytesseract.image_to_string(img)

    return captcha_text


def get_scrape(url: str):
    try:
        # Faz o request para a página
        response = requests.get(url)
        response.raise_for_status()

        # Parse o conteúdo HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Exemplo de extração de dados
        # Substitua isso com sua lógica de scraping específica
        title = soup.title.text.strip()

        # Se a página tiver um CAPTCHA, resolva-o
        captcha_img = soup.find("img", {"class": "captcha-img"})
        if captcha_img:
            captcha_image_url = "https://example.com" + captcha_img["src"]
            captcha_result = resolve_captcha(captcha_image_url)
            print("CAPTCHA Result:", captcha_result)

        # Vamos assumir que você deseja obter o conteúdo da tag <div> no corpo
        content = str(soup.find("div"))

        # Retorne os dados no formato do esquema ScrapeResponse
        return schemas.ScrapeResponse(title=title, content=content)

    except requests.HTTPError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"HTTP Error: {e.response.status_code}",
        )

    except requests.RequestException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Request Exception: {str(e)}",
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
