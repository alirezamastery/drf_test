from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class MarathonViewSet(ModelViewSet):
    queryset = Marathon.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MarathonReadSerializer
        return MarathonWriteSerializer


class ChallengeViewSet(ModelViewSet):
    queryset = Marathon.objects.all()
    serializer_class = ChallengeSerializer
