from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import DjangoModelPermissions, DjangoObjectPermissions, BasePermission
from rest_framework_guardian.filters import ObjectPermissionsFilter
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from guardian.shortcuts import remove_perm, assign_perm

from .models import *
from .serializers import *


class CanViewModel(DjangoModelPermissions):
    perms_map = {
        'GET':     ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD':    [],
        'POST':    ['%(app_label)s.add_%(model_name)s'],
        'PUT':     ['%(app_label)s.change_%(model_name)s'],
        'PATCH':   ['%(app_label)s.change_%(model_name)s'],
        'DELETE':  ['%(app_label)s.delete_%(model_name)s'],
    }


class CustomObjectPermissions(DjangoObjectPermissions):
    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """
    perms_map = {
        'GET':     ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD':    ['%(app_label)s.view_%(model_name)s'],
        'POST':    ['%(app_label)s.add_%(model_name)s'],
        'PUT':     ['%(app_label)s.change_%(model_name)s'],
        'PATCH':   ['%(app_label)s.change_%(model_name)s'],
        'DELETE':  ['%(app_label)s.delete_%(model_name)s'],
    }


class CustomerAccessPermission(BasePermission):

    def has_permission(self, request, view):
        print(f'has_permission | custom:', request.user.username)
        print(f'has_permission | {view = }')
        if request.user.username == 'alirez':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        print(f'{obj = }')
        if '2' in obj.title:
            return False
        return True


class BlogPostViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # permission_classes = [CanViewModel]
    permission_classes = [CustomObjectPermissions]
    filter_backends = [ObjectPermissionsFilter]

    def list(self, request, *args, **kwargs):
        print(f'user: {request.user} | perm: {request.user.has_perm("permission.view_blogpost")}')
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(pk=2)
        instance = self.get_object()
        print(f'user: {user} | perm: {user.has_perm("permission.view_blogpost", instance)}')
        return super().retrieve(request, *args, **kwargs)


class UpdatePermission(APIView):

    def post(self, request):
        user_id = request.data.get('user_id')
        obj_id = request.data.get('obj_id')
        has_permission = request.data.get('has_permission')
        print(f'{user_id = } | {obj_id = } | {has_permission = }')
        user = get_object_or_404(User, pk=user_id)
        obj = get_object_or_404(BlogPost, pk=obj_id)
        if has_permission is True:
            assign_perm('view_blogpost', user, obj)
        else:
            remove_perm('view_blogpost', user, obj)
        return Response({'info': 'ok'})


class UserPermissionsView(APIView):

    def get(self, request):
        print('user:', request.user)
        print('perms:', request.user.user_permissions.all())
        perms = Permission.objects.all()
        print(perms)
        for p in perms:
            print(f'{p.codename:<20} | {p.content_type.app_label:<20} | {p.content_type.model}')
        res = []
        for perm in request.user.user_permissions.all():
            res.append({
                'name': perm.name,
                'code': perm.codename,
            })
        return Response(res)
