import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

API_KEY = os.getenv("API_KEY")
MAX_ARTICLES = 20

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