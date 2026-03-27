import json
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Author:
    id: int
    name: str
    nationality: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "Author":
        return cls(
            id=data["id"],
            name=data["name"],
            nationality=data.get("nationality"),
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
    def from_dict(cls, data: dict) -> "Book":
        return cls(
            id=data["id"],
            title=data["title"],
            author_id=data["author_id"],
            year=data.get("year"),
            genre=data.get("genre"),
            available=data.get("available", True),
        )


def load_authors() -> List[Author]:
    with open("data/authors.json", "r") as f:
        data = json.load(f)
    return [Author.from_dict(item) for item in data]


# Helper functions
# These will only be useful while we work with JSON files instead of a database


def save_authors(authors: List[Author]) -> None:
    data = [
        {
            "id": a.id,
            "name": a.name,
            "nationality": a.nationality,
        }
        for a in authors
    ]
    with open("data/authors.json", "w") as f:
        json.dump(data, f, indent=2)


def get_all_authors() -> List[Author]:
    return load_authors()


def get_author_by_id(author_id: int) -> Optional[Author]:
    return next((a for a in load_authors() if a.id == author_id), None)


def add_author(
    name: str,
    nationality: Optional[str] = None,
) -> Author:
    authors = load_authors()
    new_id = max((a.id for a in authors), default=0) + 1
    new_author = Author(
        id=new_id,
        name=name,
        nationality=nationality,
    )
    authors.append(new_author)
    save_authors(authors)
    return new_author


def update_author(
    author_id: int,
    name: str,
    nationality: Optional[str] = None,
) -> Optional[Author]:
    authors = load_authors()
    for author in authors:
        if author.id == author_id:
            author.name = name
            author.nationality = nationality
            save_authors(authors)
            return author
    return None


def delete_author(author_id: int) -> bool:
    authors = load_authors()
    filtered = [a for a in authors if a.id != author_id]
    if len(filtered) == len(authors):
        return False
    save_authors(filtered)
    return True


def load_books() -> List[Book]:
    with open("data/books.json", "r") as f:
        data = json.load(f)
    return [Book.from_dict(item) for item in data]


def save_books(books: List[Book]) -> None:
    data = [
        {
            "id": b.id,
            "title": b.title,
            "author_id": b.author_id,
            "year": b.year,
            "genre": b.genre,
            "available": b.available,
        }
        for b in books
    ]
    with open("data/books.json", "w") as f:
        json.dump(data, f, indent=2)


def get_all_books() -> List[Book]:
    return load_books()


def get_book_by_id(book_id: int) -> Optional[Book]:
    return next((b for b in load_books() if b.id == book_id), None)


def add_book(
    title: str,
    author_id: int,
    year: Optional[int] = None,
    genre: Optional[str] = None,
    available: bool = True,
) -> Book:
    books = load_books()
    new_id = max((b.id for b in books), default=0) + 1
    new_book = Book(
        id=new_id,
        title=title,
        author_id=author_id,
        year=year,
        genre=genre,
        available=available,
    )
    books.append(new_book)
    save_books(books)
    return new_book


def update_book(
    book_id: int,
    title: str,
    author_id: int,
    year: Optional[int] = None,
    genre: Optional[str] = None,
    available: bool = True,
) -> Optional[Book]:
    books = load_books()
    for book in books:
        if book.id == book_id:
            book.title = title
            book.author_id = author_id
            book.year = year
            book.genre = genre
            book.available = available
            save_books(books)
            return book
    return None


def delete_book(book_id: int) -> bool:
    books = load_books()
    filtered = [b for b in books if b.id != book_id]
    if len(filtered) == len(books):
        return False
    save_books(filtered)
    return True


def get_books_with_authors() -> List[Book]:
    authors = load_authors()
    books = load_books()

    author_lookup = {author.id: author for author in authors}

    for book in books:
        book.author = author_lookup.get(book.author_id)

    return books
