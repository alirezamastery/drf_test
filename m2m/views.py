from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GroupReadSerializer
        return GroupWriteSerializer
