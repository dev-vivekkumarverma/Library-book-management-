from django.urls import path,include
from .views import book_recommendations,student_recommendations

urlpatterns = [
    path("books/",book_recommendations, name="book_recommendations_view"),
    path("student/",student_recommendations, name="student_recommendations_view"),
]
