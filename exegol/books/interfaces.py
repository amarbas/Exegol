import uuid
from typing import Dict

from authors.api import AuthorApi
from authors.models import Author


def update_author_name(*, author_name: str, author_id: uuid.UUID) -> None:
    AuthorApi.update_author_name(
        id=author_id,
        name=author_name,
    )

def get_author(*, id: uuid.UUID) -> Author:
    return AuthorApi.get_author(id=id)
