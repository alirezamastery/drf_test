from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Example
from .serializers import ExampleSerializer


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer

    @action(detail=False, methods=['get'])
    def test(self, request):
        return Response({'ok': 'test'}, 200)

    @action(detail=True, methods=['get', 'post'])
    def test_2(self, request, pk):
        return Response({'pk': pk}, 200)
