from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from userHandler.models import Student
from bookHandler.models import Book, BookBorrowDetails, BookStatistics
from userHandler.serializer import StudentSerializer
from bookHandler.serializer import BookSerializer,BookBorrwDetailsSerializer,BookStatisticsSerializer
from connectionHandler.models import Connection
from connectionHandler.serializer import ConnectionSerializer
from django.db.models import Count
# Create your views here.


# function to give book recommendation based on student's interesting Genre+++
@api_view(["GET"])
def book_recommendations(request):
    try:
        roll_number=request.data.get("roll_number","")
        if roll_number is "":
            raise Exception("Some fields are missing...")
        student=Student.objects.get(roll_number=roll_number)
        studetnt_interesting_genre=BookBorrowDetails.objects.filter(student=student).values('book__genre').annotate(total=Count("book__genre")).order_by('-total')[:3] # finding top three genres of a student's interest
        books=Book.objects.filter(genre__in=[obj['book__genre'] for obj in studetnt_interesting_genre]) #findig all the top genre books of a student
        serialized_book_data=BookSerializer(books,many=True)
        return Response(data={"data":serialized_book_data.data}, status= status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)


#function for student recomendation
@api_view(["GET"])
def student_recommendations(request):
    try:
        roll_number=request.data.get("roll_number","")
        if roll_number is "":
            raise Exception("Some fields are missing...")
        student=Student.objects.get(roll_number=roll_number)
        mutuallyconnectedpeople=Connection.objects.filter(requested_by=student,is_approved=True) # finding students who can act like mutual connection
        connectionsOfMutuallyConnecedPeople=Connection.objects.filter(requested_by__id__in=[connection.requested_for.id for connection in mutuallyconnectedpeople],is_approved=True) #finding all the connections of the mutually connected students
        newsuggestions=[user.requested_for for user in connectionsOfMutuallyConnecedPeople if user.is_approved] #extracting all the users from the connections
        serialized_data=StudentSerializer(newsuggestions,many=True) #seriallizing all the sutudent data.
        return Response(data={"data":serialized_data.data}, status= status.HTTP_200_OK)
    except Exception as e:
        return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)