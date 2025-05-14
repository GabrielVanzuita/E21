import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

API_KEY = os.getenv("API_KEY")
MAX_ARTICLES = 20

if not API_KEY:
    raise ValueError(" NEWSAPI_KEY não encontrada. Verifique seu arquivo .env.")

