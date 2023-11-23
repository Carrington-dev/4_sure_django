from rest_framework.serializers import ModelSerializer
from account.models import User

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

class XUserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')