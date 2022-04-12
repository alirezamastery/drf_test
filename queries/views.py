import datetime
from itertools import chain

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Parent, Child, SelfReference
from .serializers import ParentSerializer, ChildSerializer, SelfReferenceSerializer, FieldNameChangeSerializer


class Responder(APIView):
    def get(self, request):
        # parent = Parent.objects.first()
        data = {
            'parent': 1,
        }
        serializer = ChildSerializer(data=data)
        if serializer.is_valid():
            print('is valid')
            result = serializer.save()
            print(result.parent)
            # print(result)
        return Response({'child': 'ok'}, 200)


class SelfReferenceView(APIView):
    def get(self, request):
        objs = SelfReference.objects.all().select_related('parent')
        res_serializer = SelfReferenceSerializer(objs, many=True)
        print(objs[0])

        # data = {
        #     'name': str(datetime.datetime.now()),
        #     # 'parent': 10
        #     # 'parent': objs[0]
        #     # 'parent_id': 1
        # }
        # serializer_create = SelfReferenceSerializer(data=data)
        # if serializer_create.is_valid(raise_exception=True):
        #     res = serializer_create.save(
        #         parent=objs[2]
        #         # parent=None
        #     )
        #     print(res)
        #     print(serializer_create.data)
        # SelfReference.objects.create(name=str(datetime.datetime.now()), parent=objs[0])
        return Response(res_serializer.data, 200)


class BeforeAfterItemsView(APIView):
    def get(self, request):
        obj = SelfReference.objects.get(id=10)
        pre_objs = SelfReference.objects.filter(id__lt=10).order_by('-id')[:5]
        pre_objs_ascending = list(reversed(pre_objs))
        print(f'{pre_objs.count()} | {type(pre_objs_ascending)}')
        following_obj = SelfReference.objects.filter(id__gte=10).order_by('id')[:5]
        range_objects = list(chain(pre_objs_ascending, following_obj))
        print(range_objects)
        # serializer = SelfReferenceSerializer(pre_objs,many=True)
        serializer = SelfReferenceSerializer(range_objects, many=True)
        print(f'type: {type(serializer.data)} | {isinstance(serializer.data, list)}')
        response = {
            # 'obj':      obj,
            'pre_objs': serializer.data,
        }
        return Response(response, 200)


class FieldNameChangeView(APIView):
    def get(self, request):
        obj = SelfReference.objects.first()
        serializer = FieldNameChangeSerializer(obj)
        print(f'type: {type(serializer.data)} | {isinstance(serializer.data, list)}')
        response = {
            'obj': serializer.data,
        }
        return Response(response, 200)


class CreateSelfView(APIView):
    def get(self, request):
        parent = SelfReference.objects.first()
        # obj = SelfReference.objects.create(name='chaikin', parent=parent)
        obj = SelfReference.objects.create(name='chaikin', parent_id=7)
        # obj.parent = parent
        # obj.save()
        serializer = FieldNameChangeSerializer(obj)
        print(f'type: {type(serializer.data)} | {isinstance(serializer.data, list)}')
        response = {
            'obj': serializer.data,
        }
        return Response(response, 200)


class MultipleFilesView(APIView):

    def post(self, request):
        print(request.data)
        print(request.data.get('images'))
        # print(request.data.lists())
        for item in request.data.lists():
            print(item)
        data = dict(request.data.lists())
        print(data)
        for img in data['images']:
            print(img)
        return Response({'info': 'ok'})
