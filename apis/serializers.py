from rest_framework import serializer

from books.models import Book

class BookSerializer(serializer.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "subtitle", "author", "isbn")