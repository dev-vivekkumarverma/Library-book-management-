from django.urls import path
from .views import BookListCreateView,BookBulk,AutoComplete,borrow_book,enroll_books,return_book
urlpatterns = [
    path('',BookListCreateView.as_view(),name="all_books_view"),
    path('bulk_create/',BookBulk.as_view(),name="bulk_book_operation_view"),
    path('autocomplete/<str:searchData>',AutoComplete.as_view(),name="autocomplete_books"),
    path('borrow/',borrow_book,name="borrow_book_view"),
    path('enroll/',enroll_books,name="enroll_new_book_view"),
    path('return/',return_book,name="return_book_view"),
]
