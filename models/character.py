from pydantic import BaseModel, Field


class Character(BaseModel):
    id: str = Field(alias="_id")
    name: str
    wiki_url: str | None = Field(alias="wikiUrl", default=None)
    race: str | None = None
    birth: str | None = None
    gender: str | None = None
    death: str | None = None
    hair: str | None = None
    height: str | None = None
    realm: str | None = None
    spouse: str | None = None

    def __str__(self) -> str:
        race = self.race or "Unknown"
        gender = self.gender or "Unknown"

        return f"Name: {self.name} (Race: {race}, Gender: {gender})"