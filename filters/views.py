from django.shortcuts import render
import json
from pprint import pprint
from urllib.parse import unquote
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from django_filters import rest_framework as filters

from .models import Marathon
from .serializers import MarathonSerializer


def extract_json_from_request(request) -> dict:
    url = request.get_full_path()
    url_unquoted = unquote(url)
    if '?filter=' in url_unquoted:
        json_txt = url_unquoted.split('?filter=')[1]
        return json.loads(json_txt)
    return {}


class MarathonView(GenericAPIView):

    def get(self, request):
        pprint(extract_json_from_request(request))

        serializer = MarathonSerializer(extract_json_from_request(request))
        # if not serializer.is_valid():
        #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        print('ser data:', serializer.data)
        return Response({}, status.HTTP_200_OK)


class MarathonFilter(filters.FilterSet):
    start_date = filters.DateTimeFilter(field_name="start_date", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="end_date", lookup_expr='lte')
    title = filters.CharFilter(field_name="title", lookup_expr='contains')

    class Meta:
        model = Marathon
        fields = ['title', 'start_date', 'end_date']


class MarathonViewSet(ReadOnlyModelViewSet):
    serializer_class = MarathonSerializer
    queryset = Marathon.objects.all()
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = MarathonFilter
