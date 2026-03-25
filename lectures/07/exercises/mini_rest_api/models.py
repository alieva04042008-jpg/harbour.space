from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Movie(Base):
    __tablename__ = "movies"

    id           = Column(Integer, primary_key=True, index=True)
    title        = Column(String, nullable=False)
    imdb_rating  = Column(Float)
    main_actor   = Column(String)