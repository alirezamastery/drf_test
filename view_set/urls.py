from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import ExampleViewSet , MessageViewSet


router = DefaultRouter()
router.register(r'example', ExampleViewSet)
router.register(r'msg', MessageViewSet)
urlpatterns = router.urls
