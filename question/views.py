from .models import Post, Category

from django.contrib.auth import get_user_model

from .serializers import PostSerializer, CategorySerializer, UserSerializer

from rest_framework.viewsets import ModelViewSet


class UserView(ModelViewSet):
    queryset = get_user_model().objects.all()

    serializer_class = UserSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()

    serializer_class = CategorySerializer


class PostView(ModelViewSet):
    queryset = Post.objects.all()

    serializer_class = PostSerializer

    filterset_fields = ['status', 'author__username']

    search_fields = ['title', 'body', 'author__username']

    ordering_fields = ['status', 'published']

    ordering = ['-published']
