"""
Django settings for drf_test project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#&_ktj6bq7_kd+bi!u*7n+nua1o1_onqw&@fa5(q#$q8i#5pz8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'constance',
    'constance.backends.database',
    'guardian',

    'queries.apps.QueriesConfig',
    'view_set.apps.ViewSetConfig',
    'writable_nested.apps.WritableNestedConfig',
    'filters.apps.FiltersConfig',
    'auth_test.apps.AuthTestConfig',
    'm2m_through.apps.M2MThroughConfig',
    'm2m.apps.M2MConfig',
    'bulk_update.apps.BulkUpdateConfig',
    'question',
    'permission',
    'versioning',
    'serialize',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'versioning.middlewares.SimpleMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drf_test.urls'

TEMPLATES = [
    {
        'BACKEND':  'django.template.backends.django.DjangoTemplates',
        'DIRS':     [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS':  {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'drf_test.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':   BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES':     (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_RENDERER_CLASSES':       [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    # 'DEFAULT_SCHEMA_CLASS':           'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_SCHEMA_CLASS':           'drf_spectacular.openapi.AutoSchema',
    'EXCEPTION_HANDLER':              'drf_test.views.custom_exception_handler',
    'DEFAULT_VERSIONING_CLASS':       'rest_framework.versioning.NamespaceVersioning'
}
INTERNAL_IPS = [
    '127.0.0.1',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME':           timedelta(days=7),
    'REFRESH_TOKEN_LIFETIME':          timedelta(days=14),
    'ROTATE_REFRESH_TOKENS':           False,
    'BLACKLIST_AFTER_ROTATION':        True,
    'UPDATE_LAST_LOGIN':               False,

    'ALGORITHM':                       'HS256',
    'SIGNING_KEY':                     SECRET_KEY,
    'VERIFYING_KEY':                   None,
    'AUDIENCE':                        None,
    'ISSUER':                          None,
    'JWK_URL':                         None,
    'LEEWAY':                          0,

    'AUTH_HEADER_TYPES':               ('Bearer',),
    'AUTH_HEADER_NAME':                'HTTP_AUTHORIZATION',
    'USER_ID_FIELD':                   'id',
    'USER_ID_CLAIM':                   'user_id',
    'USER_AUTHENTICATION_RULE':        'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES':              ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM':                'token_type',

    'JTI_CLAIM':                       'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME':          timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME':  timedelta(days=1),
}

SPECTACULAR_SETTINGS = {
    'SCHEMA_PATH_PREFIX':   r'/api/*',
    'SERVE_INCLUDE_SCHEMA': False
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'Instagram': ('', 'URL', str),
}

# CONSTANCE_CONFIG = {
#     'SITE_NAME': ('My Title', 'Website title'),
#     'SITE_DESCRIPTION': ('', 'Website description'),
#     'THEME': ('light-blue', 'Website theme'),
# }
#
# CONSTANCE_CONFIG_FIELDSETS = {
#     'General Options': ('SITE_NAME', 'SITE_DESCRIPTION'),
#     'Theme Options': ('THEME',),
# }

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
]
