from pydantic import BaseModel, Field

class Quote(BaseModel):
    id: str = Field(alias="_id")
    dialog: str
    movie_id: str = Field(alias="movie")
    character_id: str = Field(alias="character")
    character_name: str = Field(default="")

    def __str__(self) -> str:
        return f"{self.character_name}: {self.dialog}"