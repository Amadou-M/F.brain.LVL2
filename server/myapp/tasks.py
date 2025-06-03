from celery import shared_task
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@shared_task
def get_password_hash(password):
    return pwd_context.hash(password)

@shared_task
def add_book_async(title, author, isbn):
    from .models import Book
    Book.objects.create(title=title, author=author, isbn=isbn)