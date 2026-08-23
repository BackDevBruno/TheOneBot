import requests as req
from models.character import Character
from models.quote import Quote
from os import getenv
from dotenv import load_dotenv

load_dotenv()

_base_url = "https://the-one-api.dev/v2"
_token = getenv("AUTH_TOKEN")
if _token is None or _token.strip() == "":
    raise Exception("API Auth token not set.")

def fetch_characters() -> list[Character]:
    res = req.get(
        f"{_base_url}/character", 
        headers={"Authorization": f"Bearer {_token}"}
    )
    if res.status_code != 200:
        raise req.HTTPError(f"Error fetching characters: {res.content}")

    return [Character(**item) for item in res.json()["docs"]]

def fetch_quotes() -> list[Quote]:
    res = req.get(
        f"{_base_url}/quote", 
        headers={"Authorization": f"Bearer {_token}"}
    )
    if res.status_code != 200:
        raise req.HTTPError(f"Error fetching quotes: {res.content}")

    return [Quote(**item) for item in res.json()["docs"]]