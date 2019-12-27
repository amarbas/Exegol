import logging
import uuid
from typing import Dict

from . import interfaces
from .models import Book


def get_books():
    return Book.objects.all()


def get_book(*, id: uuid.UUID) -> Book:
    book = Book.objects.get(id=id)
    author = interfaces.get_author(id=book.author_id)
    
    return {
        'id': book.id,
        'name': book.name,
        'author_name': author.name,
    }

def create_book(*, name: str, author_id: uuid.UUID) -> Book:
    book = Book.objects.create(name=name, author_id=author_id)
    author = interfaces.get_author(id=book.author_id)

    return {
        'id': book.id,
        'name': book.name,
        'author_name': author.name
    }


def delete_book(*, id: uuid.UUID) -> None:
    book = Book.objects.get(id=id)
    book.delete()