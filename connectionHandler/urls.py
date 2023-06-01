from django.urls import path,include
from .views import AllConnection,GetAllConnectionByIDRequest,CreateConnection,approve_connections,remove_connection_by_id

urlpatterns = [
    path('',AllConnection.as_view(),name="all_connections_view"),
    path('<int:studentID>/',GetAllConnectionByIDRequest,name="all_connection_request_for_a _strudent"),
    path('create/',CreateConnection.as_view(),name="Create_connection_view"),
    path('approve/<int:studentID>/<int:connectionID>/',approve_connections,name="approve_connection_view"),
    path('remove/<int:studentID>/<int:connectionID>/',remove_connection_by_id,name="remove connection view"),
]
