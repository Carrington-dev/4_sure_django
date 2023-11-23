import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from account.mixins import UserMixin, UserMixinVerify
from account.models import User 
from account.serializers import UserModelSerializer
from rest_framework.parsers import JSONParser

@api_view()
def home(request):
    serializer =  UserModelSerializer(User.objects.all(), many=True)
    return Response({"users": serializer.data}, status=HTTP_200_OK)


class UserCreateViewSet(UserMixin):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()

# class UserVerifyViewSet(UserMixinVerify):
#     serializer_class = UserModelSerializer
#     queryset = User.objects.all()


# @api_view(['GET', 'POST'])
# def login(request):

#     data = JSONParser().parse(request)
#     print(data)
#     serializer = UserModelSerializer(data=data)

#     user = get_object_or_404(User, email=data.get('email'))

#     print(user.check_password(data.get('password')))
#     if user.check_password(data.get('password')):
#         return Response({'message': 'Login successful', "data": data})
    
#         # return JsonResponse(serializer.data, status=201)
#     if serializer.is_valid():
#         return Response(serializer.data, status=400)
#     return Response({"message": "Not logged in"})

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        return JsonResponse({"message": "Not logged in", **data})
    return JsonResponse({"message": "Not logged in"})