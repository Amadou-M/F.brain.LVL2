from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('books/', views.book_list, name='book_list'),
]