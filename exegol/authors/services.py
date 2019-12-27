import logging
import uuid
from typing import Dict

from . import interfaces
from .models import Author


def get_authors():
    return Author.objects.all()


def get_author(*, id: uuid.UUID) -> Dict:
    author = Author.objects.get(id=id)
    
    return {
        'id': author.id,
        'name': author.name
    }

def create_author(*, name: str) -> Author:
    author = Author.objects.create(name=name)

    return author


def delete_author(*, id: uuid.UUID) -> None:
    author = Author.objects.get(id=id)
    author.delete()