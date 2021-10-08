from .serializers import UserSerializer
from rest_framework.viewsets import ModelViewSet
from .models import UserBase


class UserViewSet(ModelViewSet):
    queryset = UserBase.objects.all()
    serializer_class = UserSerializer

    
