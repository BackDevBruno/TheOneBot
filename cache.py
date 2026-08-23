from models.character import Character
from models.quote import Quote
import api_requests as req

characters = []
characters_by_id = {}
quotes = []

def _load_character_data():
    global characters
    characters = req.fetch_characters()
    characters.sort(key=lambda c: c.name)

    global characters_by_id
    characters_by_id = {c.id: c for c in characters}

def _load_quote_data():
    _load_character_data()

    global quotes
    quotes = req.fetch_quotes()
    for i, q in enumerate(quotes):
        c = characters_by_id.get(q.character_id)
        if c is not None:
            quotes[i].character_name = c.name
    quotes.sort(key=lambda q: q.character_name)

def get_characters() -> list[Character]:
    if characters == []:
        _load_character_data()

    return characters

def get_characters_by_name(name: str) -> list[Character]:
    name = name.strip().lower()
    if name == "":
        return []

    if characters == []:
        _load_character_data()

    return [c for c in characters if c.name.strip().lower().find(name) != -1]

def get_quotes() -> list[Quote]:
    if quotes == []:
        _load_quote_data()

    return quotes

def get_quotes_by_character(character_name: str) -> list[Quote]:
    character_name = character_name.strip().lower()
    if character_name == "":
        return []

    if quotes == []:
        _load_quote_data()

    characters = get_characters_by_name(character_name)
    if characters == []:
        return []

    c_quotes = []
    for character in characters:
        c_quotes.append([q for q in quotes if q.character_id == character.id])

    return c_quotes