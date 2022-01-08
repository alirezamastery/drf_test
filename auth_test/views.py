from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import (
    extend_schema, extend_schema_view, OpenApiExample, OpenApiParameter
)
from drf_spectacular.openapi import OpenApiTypes

from .models import SignUpToken


class AllowAnyView(GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        print(request.user)
        return Response({'ok': 'ok'}, status.HTTP_200_OK)


class TestRequestSerializer(serializers.Serializer):
    test = serializers.CharField()


class TestQuerySerializer(serializers.Serializer):
    param = serializers.CharField()


class VerifySignUp(GenericAPIView):

    @extend_schema(
        parameters=[
            TestQuerySerializer,  # serializer fields are converted to parameters
            OpenApiParameter("nested", TestQuerySerializer),  # serializer object is converted to a parameter
            OpenApiParameter(
                "chaikin_param_1",
                OpenApiTypes.UUID,
                OpenApiParameter.QUERY,
                description='chaikin_param_1 description',
                examples=[OpenApiExample(name='chaikin 1 example', value='ccc')]
            ),
            OpenApiParameter("pk", OpenApiTypes.UUID, OpenApiParameter.PATH),  # path variable was overridden
        ],
        request=TestRequestSerializer,
        responses=TestRequestSerializer,
        # more customizations
    )
    def get(self, request):
        token = request.GET.get('token')
        print(token)
        verfy_obj = SignUpToken.objects.filter(token=token).first()
        print(verfy_obj)
        # verfy_obj.user.is_admin = False
        # verfy_obj.user.save()
        user_obj = verfy_obj.user
        print(user_obj)
        user_obj.is_active = True
        user_obj.save()
        return Response({'info': 'ok'}, 200)
