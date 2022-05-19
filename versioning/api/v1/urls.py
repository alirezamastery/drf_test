from rest_framework.routers import DefaultRouter

from .views import BlogViewSetVersion1


app_name = 'versioning'

router = DefaultRouter()

router.register('blogs', BlogViewSetVersion1)

urlpatterns = router.urls
