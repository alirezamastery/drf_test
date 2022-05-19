from rest_framework.viewsets import ModelViewSet

from versioning.models import Blog
from .serializers import BlogSerializerVersion2


class BlogViewSetVersion2(ModelViewSet):
    queryset = Blog.objects.all().order_by('id')
    serializer_class = BlogSerializerVersion2
