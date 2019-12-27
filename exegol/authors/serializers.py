from rest_framework import serializers


class AuthorDetailSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
