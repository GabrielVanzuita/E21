import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

API_KEY = os.getenv("API_KEY")
MAX_ARTICLES = 20
url:

if not API_KEY:
    raise ValueError(" NEWSAPI_KEY não encontrada. Verifique seu arquivo .env.")

def get_noticias (url,API_KEY):
    params = {
        "q": topic,
        "pageSize": limit,
        "sortBy": "publishedAt",
        "apiKey": API_KEY,
        "language": "eng"
    }

    response = requests.get(url, params = params)

    data = response.json()

    if response.status_code != 200 or "articles" not in data:
        print("rro ao buscar notícias:", data.get("message", "Erro desconhecido"))
        return []

    return data["articles"]

while True:
    print ('\n PESQUISA DE NOTÍCIAS')
    topic = input ("Digite um tema para buscar ou 'Sair', para sair.").lower()
    max_articles = 10
    if topic == "sair":
        break
    else:
        try:
            limit = int (input(f"Quantas notícias você deseja visualizar?Máximo de {max_articles}:")
        except ValueError:
            if limit > 10 or limit < 1:
                print ("Número de notícias exibidas é inválido. Por favor, escolha um número entre 1 e 10")
            else:
                print("Apenas números são permitidos")
                continue

        articles = get_noticias(url=url, API_KEY=API_KEY)

