from rest_framework.serializers import ModelSerializer

from versioning.models import Blog


class BlogSerializerVersion2(ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'image']
