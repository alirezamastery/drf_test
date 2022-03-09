from rest_framework.routers import DefaultRouter

from .views import *


router = DefaultRouter()

urlpatterns = []

router.register('category', CategoryView)
router.register('post', PostView)
urlpatterns += router.urls
