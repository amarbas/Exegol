import uuid

from django.db import models


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256)
    publisher = models.CharField(max_length=256)
    author = models.ForeignKey('authors.Author', related_name='books', on_delete=models.CASCADE)

    class Meta:
        db_table = 'books'

    @property
    def name_and_publisher(self):
        return f'{self.name}, {self.publisher}'
