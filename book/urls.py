from django.contrib import admin
from django.urls import path, include
from book.views import home, store_book, show_book, edit_book, delete_book

urlpatterns = [
    path('', home, name='homepage'),
    path('store_book/', store_book, name='store_book'),
    path('show_book/', show_book, name='show_book'),
    path('edit_book/<int:id>', edit_book, name='edit_book'),
    path('delete_book/<int:id>', delete_book, name='delete_book'),
]