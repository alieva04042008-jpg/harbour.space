from pydantic import BaseModel

class MovieCreate(BaseModel):
    title: str
    imdb_rating: float
    main_actor: str

class MovieResponse(MovieCreate):
    id: int

    class Config:
        from_attributes = True