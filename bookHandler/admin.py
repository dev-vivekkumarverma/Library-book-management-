from django.contrib import admin
from .models import Book,BookBorrowDetails,BookStatistics
# Register your models here.


admin.site.register(Book)
admin.site.register(BookBorrowDetails)
admin.site.register(BookStatistics)