from django.test import TestCase
from .models import Book

class BookTests(TestCase):
    def setUp(self):
        Book.objects.create(title="Test Book", author="Test Author", isbn="1234567890123")

    def test_book_str(self):
        book = Book.objects.get(isbn="1234567890123")
        self.assertEqual(str(book), "Test Book")