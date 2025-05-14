import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

API_KEY = os.getenv("API_KEY")
MAX_ARTICLES = 20
url = "https://newsapi.org/v2/everything"

if not API_KEY:
    raise ValueError(" NEWSAPI_KEY não encontrada. Verifique seu arquivo .env.")

def get_noticias (topic, limit):
    params = {
        "q": topic,
        "pageSize": limit,
        "sortBy": "publishedAt",
        "apiKey": API_KEY,
        "language": "en"
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
            limit = int(input(f"Quantas notícias deseja ver? (1 a {MAX_ARTICLES}): "))
            if limit < 1 or limit > MAX_ARTICLES:
                print(f"⚠️ Escolha um número entre 1 e {MAX_ARTICLES}.")
                continue
        except ValueError:
            print("⚠️ Apenas números são permitidos.")
            continue

        articles = get_noticias(topic, limit)

        if not articles:
            print("Nenhuma notícia encontrada.")
        else:
            for i, art in enumerate(articles, 1):
                print(f"\n[{i}] 📰 {art.get('title')}")
                print(f"    🏷️ Fonte: {art.get('source', {}).get('name')}")
                print(f"    ✍️ Autor: {art.get('author') or 'Desconhecido'}")

