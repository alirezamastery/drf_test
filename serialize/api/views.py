from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *


class TestValidatedDate(APIView):

    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        print('data:', serializer.data)
        print('validated_data:', serializer.validated_data)

        return Response(serializer.data)
