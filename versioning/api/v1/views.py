from rest_framework.viewsets import ModelViewSet

from versioning.models import Blog
from .serializers import BlogSerializerVersion1
from ..v2.serializers import BlogSerializerVersion2


class BlogViewSetVersion1(ModelViewSet):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializerVersion1

    def get_serializer_class(self):
        print('v:', self.request.version)
        if self.request.version == 'v1':
            return BlogSerializerVersion1
        return BlogSerializerVersion2
