from rest_framework.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter
from .views import *


app_name = 'auth_test'

urlpatterns = [
    path('allow-any/', AllowAnyView.as_view()),
    path('signup-verify/', VerifySignUp.as_view()),
]
