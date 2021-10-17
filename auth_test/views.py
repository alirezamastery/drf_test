from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import SignUpToken


class AllowAnyView(GenericAPIView):
    permission_classes = [AllowAny]

    def get(self, request):
        print(request.user)
        return Response({'ok': 'ok'}, status.HTTP_200_OK)


class VerifySignUp(GenericAPIView):

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
