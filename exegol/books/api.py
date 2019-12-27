import logging
import uuid
from typing import Dict

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from . import services as book_service
from . import serializers


class BookApi:
    @staticmethod
    def get(*, book_id: uuid.UUID) -> Dict:
        logging.info('method "get" called')
        return book_service.get_book(id=book_id)


class BookRestApi(viewsets.ViewSet):
    def list(self, request):
        books = book_service.get_books()
        serializer = serializers.BookListSerializer(books, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        book = book_service.get_book(id=pk)
        print("Book", book)
        serializer = serializers.BookDetailSerializer(book)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        book_service.delete_book(id=pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request):
        name = request.data.get('name')
        author_id = request.data.get('author_id')
        book = book_service.create_book(name=name, author_id=author_id)
        serializer = serializers.BookDetailSerializer(book)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def authors(self, request, pk=None):
        print("UUID", pk)
        return Response([{ "id": uuid.uuid4() }, { "id": uuid.uuid4() }])
