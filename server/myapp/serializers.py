from rest_framework import serializers
from .models import Book, Borrow

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date', 'available']

class BorrowSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Borrow
        fields = ['id', 'user', 'book', 'borrow_date', 'return_date', 'returned']