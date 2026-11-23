from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional

#database table
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    email: str = Field(unique=True)
    college: str = Field(index=True)

    # one user can have many posts
    books: List["Book"] = Relationship(back_populates="owner")

#request body for creating an user
class UserCreate(SQLModel):
    name: str
    email: str
    college: str

#response model for user
class UserRead(SQLModel):
    id: int
    name: str
    email: str
    college: str



# avoid circular import error

from models.book import Book
User.model_rebuild()



