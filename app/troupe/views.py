from django.shortcuts import render
from client.models import Client
from rest_framework import generics
from troupe.permissions import IsOwnerOrReadOnly
from troupe.mixins import TroupeMixin
from troupe.serializers import TroupeModelSerializer

# Create your views here.
class AppointmentViewSet(TroupeMixin):
    serializer_class = TroupeModelSerializer
    queryset = Client.objects.all()
    # permission_classes = [ IsOwnerOrReadOnly ]


class AppointmentList(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = TroupeModelSerializer

