from rest_framework import serializers


class BookListSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()


class BookDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    author_name = serializers.CharField()
