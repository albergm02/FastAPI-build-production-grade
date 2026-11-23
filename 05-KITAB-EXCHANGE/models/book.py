from sqlmodel import SQLModel, Field, Relationship
from typing import Optional

class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    author: str = Field(index=True)
    price: int
    is_sold: bool = Field(default=False)
    #foreign key to user table
    user_id : int = Field(default=None, foreign_key="user.id")
    owner: Optional["User"] = Relationship(back_populates="books")


#request body for creating an book
class BookCreate(SQLModel):
    title: str
    author: str
    price: int

#response model for book
class BookRead(SQLModel):
    id: int
    title: str
    author: str
    price: int
    is_sold: bool

class BookUpdate(SQLModel):
    price: Optional[int] = None
    is_sold: Optional[bool] = None

#response model for user
class UserRead(SQLModel):
    id: int
    name: str
    email: str
    college: str

# avoid circular import error

from models.user import User
Book.model_rebuild()

