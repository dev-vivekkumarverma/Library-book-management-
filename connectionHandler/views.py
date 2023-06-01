from django.shortcuts import render
from .models import Connection
from .serializer import ConnectionSerializer
from rest_framework.views import Response
from rest_framework import status,generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view

# API to get all connection requests made.
class AllConnection(generics.ListAPIView):
    queryset=Connection.objects.all()
    serializer_class=ConnectionSerializer

# API view to get all the connection request details of a student
@api_view(['GET'])
def GetAllConnectionByIDRequest(request,studentID:int):
    try:
        all_connection_request=Connection.objects.filter(requested_for=studentID,is_removed=False)
        all_connection_request_serialized_data=ConnectionSerializer(all_connection_request,many=True)
        return Response(data=all_connection_request_serialized_data.data,status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)

#API view to handle approve connection requests.
@api_view(['GET'])
def approve_connections(request,studentID:int,connectionID:int):
    try:
        connection_object=Connection.objects.get(pk=connectionID)
        if connection_object.requested_for .pk== studentID and connection_object.is_approved==False and connection_object.is_removed==False:
            connection_object.is_approved=True
            connection_object.save()
            serialized_connection_data=ConnectionSerializer(connection_object)
            return Response(data=serialized_connection_data.data,status=status.HTTP_202_ACCEPTED)
        elif connection_object.requested_for.pk == studentID and connection_object.is_approved==True and connection_object.is_removed==False:
            raise Exception("Connection is already apporoved.")
        else:
            raise Exception("You are not authorized for this task...")

    except Exception as e:
        return Response(data={"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
    
class CreateConnection(generics.CreateAPIView):
    queryset=Connection.objects.all()
    serializer_class=ConnectionSerializer


#API view to remove a connection.
@api_view(["DELETE"])
def remove_connection_by_id(request, studentID:int,connectionID:int):
    try :
        connection_object=Connection.objects.get(pk=connectionID)
        if (connection_object.requested_by.id==studentID or connection_object.requested_for.id==studentID) and connection_object.is_removed==False:
            connection_object.is_removed=True
            connection_object.save()
            return Response(data={"info":"connection successfully removed.."},status=status.HTTP_200_OK)
        else:
            raise Exception("Illigal operation")
    except Exception as e:
        return Response(data={"error":str(e)},status=status.HTTP_200_OK)

