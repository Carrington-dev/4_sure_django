from rest_framework.serializers import ModelSerializer
from client.models import Client

class ClientModelSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('user', 'name', 'email', 'number')