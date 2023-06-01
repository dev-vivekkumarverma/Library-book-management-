from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
#API view for handling student registrations
class StudentRegistrationView(APIView):
    def post(self,request):
        try:
            deserialized_student_data=StudentSerializer(data=request.data)
            if deserialized_student_data.is_valid():
                deserialized_student_data.save()
                return Response({
                    "username":deserialized_student_data.data["name"],
                    "email_ID":deserialized_student_data.data["email_ID"],
                    "message":"User registration successfull !"
                    },status=status.HTTP_201_CREATED)
            else:
                return Response("User Creation Failed due to serialization...",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    # pass

# API view to get all student details. 
class StudentListView(APIView):
    def get(self,request):
        try:
            all_students=Student.objects.all()
            serialized_student_data=StudentSerializer(all_students,many=True)
            return Response(data=serialized_student_data.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

# API view for handling autocompete student while searching feature. 
class AutoComplete(APIView):
    def get(self, request, searchData:str):
        try:
            all_student=Student.objects.all().filter(name__icontains=searchData)
            all_strudent_serialize_data=StudentSerializer(all_student,many=True)
            return Response(data=all_strudent_serialize_data.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)