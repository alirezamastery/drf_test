from django.apps import AppConfig


class WritableNestedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'writable_nested'
