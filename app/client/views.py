from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet

from client.models import Client
from client.serializers import ClientModelSerializer
from client.mixins import ClientMixin

class ClientViewSet(ClientMixin):
    serializer_class = ClientModelSerializer
    queryset = Client.objects.all()