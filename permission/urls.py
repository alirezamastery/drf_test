from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *


urlpatterns = [
    path('user-perms/', UserPermissionsView.as_view()),
    path('update-perms/', UpdatePermission.as_view()),
]

router = DefaultRouter()
router.register('blogs', BlogPostViewSet)

urlpatterns += router.urls
