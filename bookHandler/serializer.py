from  .models import Book, BookBorrowDetails,BookStatistics
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"


class BookStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookStatistics
        fields="__all__"


class BookBorrwDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookBorrowDetails
        fields="__all__"
        