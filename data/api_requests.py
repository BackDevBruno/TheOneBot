import requests as req

from models.character import Character
from models.quote import Quote
from os import getenv


base_url = "https://the-one-api.dev/v2"

def get_token() -> str | None:
    return getenv("AUTH_TOKEN")

def fetch_characters() -> list[Character]:
    token = get_token()
    if token is None or token.strip() == "":
        raise Exception("API Auth token not set.")

    res = req.get(
        f"{base_url}/character", 
        headers={"Authorization": f"Bearer {token}"}
    )
    if res.status_code != 200:
        raise req.HTTPError(f"Error fetching characters: {res.content}")

    return [Character(**item) for item in res.json()["docs"]]

def fetch_quotes() -> list[Quote]:
    token = get_token()
    if token is None or token.strip() == "":
        raise Exception("API Auth token not set.")

    res = req.get(
        f"{base_url}/quote", 
        headers={"Authorization": f"Bearer {token}"}
    )
    if res.status_code != 200:
        raise req.HTTPError(f"Error fetching quotes: {res.content}")

    return [Quote(**item) for item in res.json()["docs"]]