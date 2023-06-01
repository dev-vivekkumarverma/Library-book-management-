from django.urls import path,include
from .views import StudentRegistrationView,StudentListView,AutoComplete

urlpatterns = [
    path('',StudentListView.as_view(),name="all_student_details_view"),
    path('register/',StudentRegistrationView.as_view(),name="student_registration_view"),
    path('autocomplete/<str:searchData>',AutoComplete.as_view(),name="autocomplete_books"),
]
