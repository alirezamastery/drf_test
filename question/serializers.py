from .models import Post, Category

from rest_framework import serializers

from django.contrib.auth import get_user_model


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = ["id", "name", "image"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()

        fields = ["id", "username", "email"]


class CategoryCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name", read_only=True)
    # category = CategoryCustomSerializer(many=True)
    # category = serializers.SerializerMethodField('category_names')

    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Post

        fields = "__all__"

    def category_names(self, obj):
        return obj.category.all().values_list('name', flat=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()

        fields = "__all__"
