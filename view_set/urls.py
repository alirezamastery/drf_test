from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import ExampleViewSet


router = DefaultRouter()
router.register(r'example', ExampleViewSet)
urlpatterns = router.urls
