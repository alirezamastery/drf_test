from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MarathonView, MarathonViewSet


app_name = 'chat_api'

urlpatterns = [
    path('marathon-get/', MarathonView.as_view(), name='simple_upload'),
]

router = DefaultRouter()
router.register('marathon', MarathonViewSet)

urlpatterns += router.urls
