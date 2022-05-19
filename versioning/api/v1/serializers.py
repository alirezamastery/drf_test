from rest_framework.serializers import ModelSerializer

from versioning.models import Blog


class BlogSerializerVersion1(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
