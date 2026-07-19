import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPID_API_KEY")
API_HOST = os.getenv("RAPID_API_HOST")


def fetch_live_matches():
    url = f"https://{API_HOST}/matches/v1/live"

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": API_HOST
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("API Error:", response.status_code)
        return None