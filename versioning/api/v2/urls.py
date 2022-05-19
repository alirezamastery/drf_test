from rest_framework.routers import DefaultRouter

from .views import BlogViewSetVersion2

# app_name = 'versioning2'

router = DefaultRouter()

router.register('blogs', BlogViewSetVersion2)

urlpatterns = router.urls
