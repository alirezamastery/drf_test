from django.urls.conf import path, include, re_path


# app_name = 'versioning'

urlpatterns = [
    path('v1/', include('versioning.api.v1.urls', namespace='v1')),
    path('v2/', include('versioning.api.v1.urls', namespace='v2')),
]
