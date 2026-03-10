from pydantic import BaseModel
from typing import Optional, List


# Author schemas
class AuthorBase(BaseModel):
    name: str
    nationality: Optional[str] = None
    birth_date: Optional[str] = None


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True


# Book schemas
class BookBase(BaseModel):
    title: str
    author_id: int
    year: Optional[int] = None
    genre: Optional[str] = None
    available: bool = True


class BookCreate(BookBase):
    pass


class BookUpdate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True


# Book with author info (for responses that need author details)
class BookWithAuthor(Book):
    author: Optional[Author] = None
