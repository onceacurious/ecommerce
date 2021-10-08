from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import UserBase


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserBase
        fields = ['user_name', 'email', 'password']
