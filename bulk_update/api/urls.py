from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *


app_name = 'bulk_update'

urlpatterns = [
]

router = DefaultRouter()

router.register('invoice-items', InvoiceItemViewSet, basename='invoice-items')

urlpatterns += router.urls
