from rest_framework.serializers import ModelSerializer
from .models import Connection

class ConnectionSerializer(ModelSerializer):
    class Meta:
        model=Connection
        fields="__all__"