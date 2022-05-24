from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'serialize'

urlpatterns = [
    path('validated-data-vs-data/', TestValidatedDate.as_view())
]

router = DefaultRouter()
