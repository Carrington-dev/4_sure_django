from rest_framework.serializers import ModelSerializer
from client.models import Client

class TroupeModelSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ('user', 'name', 'email', 'number')