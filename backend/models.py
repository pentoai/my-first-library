import json
from dataclasses import dataclass
from typing import List, Optional
from datetime import date


@dataclass
class Author:
    id: int
    name: str
    nationality: Optional[str] = None
    birth_date: Optional[date] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'Author':
        birth_date = None
        if data.get('birth_date'):
            birth_date = date.fromisoformat(data['birth_date'])

        return cls(
            id=data['id'],
            name=data['name'],
            nationality=data.get('nationality'),
            birth_date=birth_date
        )


@dataclass
class Book:
    id: int
    title: str
    author_id: int
    year: Optional[int] = None
    genre: Optional[str] = None
    available: bool = True
    author: Optional[Author] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        return cls(
            id=data['id'],
            title=data['title'],
            author_id=data['author_id'],
            year=data.get('year'),
            genre=data.get('genre'),
            available=data.get('available', True)
        )


def load_authors() -> List[Author]:
    with open('data/authors.json', 'r') as f:
        data = json.load(f)
    return [Author.from_dict(item) for item in data]


def load_books() -> List[Book]:
    with open('data/books.json', 'r') as f:
        data = json.load(f)
    return [Book.from_dict(item) for item in data]


def get_books_with_authors() -> List[Book]:
    authors = load_authors()
    books = load_books()

    author_lookup = {author.id: author for author in authors}

    for book in books:
        book.author = author_lookup.get(book.author_id)

    return books
