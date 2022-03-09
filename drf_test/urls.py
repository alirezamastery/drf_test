from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
import debug_toolbar
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('query/', include('queries.urls')),
    path('view_set/', include('view_set.urls')),
    path('filters/', include('filters.urls')),
    path('auth_test/', include('auth_test.urls')),
    path('api/m2m_through/', include('m2m_through.urls')),
    path('api/m2m/', include('m2m.urls')),
    path('api/bulk/', include('bulk_update.api.urls')),
    path('api/question/', include('question.urls')),

    # drf schema and docs
    path('docs/', include_docs_urls(title='Test API', public=False)),
    path('schema/', get_schema_view(
        title='My Project',
        description='a good API for a good frontend',
        version='1.0',
        # renderer_classes=[renderers.JSONOpenAPIRenderer]
    ), name='openapi-schema'),

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
