from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
import debug_toolbar

from django.views.generic import TemplateView


urlpatterns = [
    # ...

]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('query/', include('queries.urls')),
    path('view_set/', include('view_set.urls')),
    # drf schema and docs
    path('docs/', include_docs_urls(title='Test API', public=False)),
    path('schema/', get_schema_view(
        title='My Project',
        description='a good API for a good frontend',
        version='1.0',
        # renderer_classes=[renderers.JSONOpenAPIRenderer]
    ), name='openapi-schema'),
    # Route TemplateView to serve Swagger UI template.
    #   * Provide `extra_context` with view name of `SchemaView`.
    # path('swagger-ui/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url': 'openapi-schema'}
    # ), name='swagger-ui'),
]
