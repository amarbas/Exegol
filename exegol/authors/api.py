import uuid

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Author
from . import services
from . import serializers

class AuthorApi:
    @staticmethod
    def update_author_name(*, id: uuid.UUID, name: str) -> Author:
        author = Author.objects.get(id)
        author.name = name
        author.save()

        return author

    @staticmethod
    def get_author(*, id: uuid.UUID) -> Author:
        return Author.objects.get(id=id)


class AuthorRestApi(viewsets.ViewSet):
    def list(self, request):
        authors = services.get_authors()
        serializer = serializers.AuthorDetailSerializer(authors, many=True)
        return Response({
            'message': 'Success',
            'data': serializer.data,
            'errors': None
        })

    def create(self, request):
        name = request.data.get('name')
        author = services.create_author(name=name)
        serializer = serializers.AuthorDetailSerializer(author)
        return Response(serializer.data)