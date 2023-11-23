from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from client.models import Client
from client.serializers import ClientModelSerializer

class ClientViewSet(ModelViewSet):
    serializer_class = ClientModelSerializer
    queryset = Client.objects.all()