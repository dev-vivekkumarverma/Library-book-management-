import json
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Book,BookStatistics,BookBorrowDetails
from .serializer import BookSerializer,BookBorrwDetailsSerializer,BookStatisticsSerializer
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework.decorators import api_view
from userHandler.models import Student
from django.db.models import Q
# Create your views here.

# CLass based View for creating a single book and Listing all book record.
class BookListCreateView(generics.ListCreateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

# API Class based view for creating a book data,editing a book data,delete books in bulk.
class BookBulk(APIView):
    def post(self,request):
        try:
            list_book_data=request.data
            book_object_list=[Book(**kargs) for kargs in list_book_data]
            bulk_books=Book.objects.bulk_create(objs=book_object_list)
            serialized_books=BookSerializer(bulk_books,many=True)
            return Response(data={"books":serialized_books.data},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request):
        try:
            list_book_data=request.data
            book_object_list=[Book(**kargs) for kargs in list_book_data]
            Book.objects.bulk_update(objs=book_object_list,fields=[field for field in request.data[0].keys() if field !='id'])
            return Response(data={"books":"bulk update successfull"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        try:
            book_objects=Book.objects.all().filter(**request.data)
            deleted_data=book_objects.delete()
            return Response(data={"books":deleted_data},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

#API view for faciliatating autocomplete Feature while searching a BOOK
class AutoComplete(APIView):
    def get(self,request,searchData:str):
        try:
            book_objects=Book.objects.all().filter(Q(title__icontains=searchData)| Q(author__icontains=searchData)| Q(genre__icontains=searchData))
            serialized_book_data=BookSerializer(book_objects,many=True)
            return Response(data={"books":serialized_book_data.data},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

#API view to enroll a book state and get all book state information
@api_view(["POST","GET"])
def enroll_books(request):
    try:
        if request.method=="POST":
            bookId=request.data.get("book","")
            total_unit=request.data.get("total_units","")
            if all([bookId,total_unit]):
                book_object=Book.objects.get(id=bookId)
                book_objects=BookStatistics.objects.create(book=book_object,total_units=total_unit)
                books_serialized_data=BookStatisticsSerializer(book_objects)
                return Response(data=books_serialized_data.data,status=status.HTTP_201_CREATED)
            else:
                raise Exception("Some fields are missing...")
        elif request.method=="GET":
            all_book_object=BookStatistics.objects.all()
            book_stat_serialized_data=BookStatisticsSerializer(all_book_object,many=True)
            return Response(data=book_stat_serialized_data.data,status=status.HTTP_200_OK)
        else:
            raise Exception("Invalid method is Called...")
    except Exception as e:
        return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

# API view to borrow a book    
@api_view(["GET","POST"])
def borrow_book(request):
    try:
        if request.method=="GET":
            all_objects=BookBorrowDetails.objects.all()
            serialized_objects=BookBorrwDetailsSerializer(all_objects,many=True)
            return Response(data=serialized_objects.data,status=status.HTTP_200_OK)
        elif request.method=="POST":
            student_roll_number=request.data.get("roll_number","")
            bookID=request.data.get("book_id","")
            units=request.data.get("units","")
            if not all([student_roll_number,bookID]):
                raise Exception("Some fields are missing...")

            if units is '':
                units=1
            student_object=Student.objects.get(roll_number=student_roll_number)
            book_object=Book.objects.get(id=bookID)
            book_stat=BookStatistics.objects.get(book=book_object)
            if book_stat.is_available():
                book_borrow_object=BookBorrowDetails.objects.create(book=book_object,student=student_object,units=units)
                if book_stat.increase_total_used(units=units):
                    book_borrow_serialized_data=BookBorrwDetailsSerializer(book_borrow_object)
                    return Response(data=book_borrow_serialized_data.data,status=status.HTTP_201_CREATED)
                else:
                    book_borrow_object.delete()
                    raise Exception("We are not able to process Your borrow request due to some technical issues.")
            else:
                raise Exception("Book currently not available...")
    except Exception as e:
        return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

# API view to return a book.
@api_view(["PATCH"])
def return_book(request):
    try:
        student_roll_number=request.data.get("roll_number","")
        bookID=request.data.get("book_id","")
        units=request.data.get("units","")
        if not all([student_roll_number,bookID]):
            raise Exception("Some fields are missing...")

        if units is '':
            units=1

        book_object=Book.objects.get(id=bookID)
        student_object=Student.objects.get(roll_number=student_roll_number)
        book_borrow_details=BookBorrowDetails.objects.get(student=student_object,book=book_object,is_submitted=False)
        book_stat=BookStatistics.objects.get(book=book_object)
        if book_stat.decrease_total_used(units=units):
            book_borrow_details.submit_book()
            book_borrow_details.save()
            book_borrow_details_serialized_data=BookBorrwDetailsSerializer(book_borrow_details)
            return Response(data=book_borrow_details_serialized_data.data,status=status.HTTP_202_ACCEPTED)
        else:
            raise Exception("We are not able to process Your return request due to some technical issues.")

    except Exception as e:
        return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)


