from rest_framework import viewsets, pagination
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

from .models import Example, Message
from .serializers import ExampleSerializer, MessageSerializer


class MessagePagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'next':        self.get_next_link(),
            'previous':    self.get_previous_link(),
            'count':       self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'msg_list':    data
        })


class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    pagination_class = MessagePagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group_id', 'file_type']


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer

    @action(detail=False, methods=['get'])
    def test(self, request):
        return Response({'ok': 'test'}, 200)

    @action(detail=True, methods=['get', 'post'])
    def test_2(self, request, pk):
        return Response({'pk': pk}, 200)
