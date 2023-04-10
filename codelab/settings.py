"""
Django settings for codelab project.

Generated by 'django-admin startproject' using Django 3.2.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta
from google.oauth2 import service_account
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*6e2srxzduhv1k6i4lpzc8*o(jwt0k@11*qc&$b=%6@vqkw6!t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['132.145.27.253', '127.0.0.1', "192.168.1.26", '192.168.224.199', "192.168.188.41",  "192.168.188.199",  "192.168.235.199", '192.168.1.218', '192.168.85.199', '192.168.100.3', '192.168.100.128', '74.208.122.227',  '127.0.0.1', "192.168.0.107", "192.168.0.101", "192.168.0.100", "192.168.0.108",  "192.168.0.102",  "192.168.0.109",  "192.168.0.100", '192.168.0.107', 'localhost', '127.0.0.1', "codelab", "192.168.0.121", "192.168.1.46", "192.168.1.37", "192.168.1.149", "192.168.1.49", "192.168.1.19"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pal',
    'rest_framework',
    'authentication',
    'rest_framework.authtoken',
    'rest_auth',
    'django.contrib.sites',
    'dj_rest_auth',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'tinymce',
    'channels',
    'school',

]
SITE_ID = 1


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': ("rest_framework.renderers.JSONRenderer",),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.BasicAuthentication',

    ),
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny'
     ],
    # 'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    # 'COERCE_DECIMAL_TO_STRING': False,

}

AUTHENTICATION_BACKENDS = [
    # allauth specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    # Needed to login by username in Django admin, regardless of allauth
    'django.contrib.auth.backends.ModelBackend',
]

REST_USE_JWT = True
JWT_AUTH_COOKIE = 'my-app-auth' # The cookie key name can be the one you want
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pal.request_interceptor.simple_middleware',  # here your middleware

]

ROOT_URLCONF = 'codelab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'pal/templates'),  # Add this inside the DIRS li
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'codelab.wsgi.application'
ASGI_APPLICATION = 'codelab.routing.application'
# ASGI_APPLICATION = 'codelab.asgi.application'

# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [('0.0.0.0', 6379)],
#         },
#     },
# }

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     # 'ENGINE': 'django.db.backends.sqlite3',
    #     # 'NAME': BASE_DIR / 'db.sqlite3',
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'dfPd6dfTEfgds5',
    #     'USER': 'root',
    #     # 'PASSWORD': 'df@Pd6dfTEfgds5',
    #     'PASSWORD': '!Ivers@l',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         'autocommit': True,
    #     },
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dfPd6dfTEfgdsclab2',
        'USER': 'postgres',
        'PASSWORD': '!Ivers@l',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
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
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'authentication.CustomUser'

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_CONFIRM_EMAIL_ON_GET = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.office365.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'your email host user'
# EMAIL_HOST_PASSWORD = 'your email host password'

REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'authentication.serializers.CustomRegisterSerializer',
}

REST_AUTH_SERIALIZERS = {
    # 'USER_DETAILS_SERIALIZER': 'authentication.serializers.CustomRegisterSerializer',
    'USER_DETAILS_SERIALIZER': 'authentication.serializers.CustomUserDetailsSerializer',
    'PASSWORD_RESET_SERIALIZER': 'authentication.serializers.CustomUserDetailsSerializer',
}
LOGIN_URL = 'http://127.0.0.1:8000/auth/login/'


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=250),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=300),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    # 'VERIFYING_KEY': None,
    # 'AUDIENCE': None,
    # 'ISSUER': None,
    # 'JWK_URL': None,
    # 'LEEWAY': 0,
    #
    # 'AUTH_HEADER_TYPES': ('Bearer',),
    # 'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    # 'USER_ID_FIELD': 'id',
    # 'USER_ID_CLAIM': 'user_id',
    # 'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',
    #
    # 'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    # 'TOKEN_TYPE_CLAIM': 'token_type',
    #
    # 'JTI_CLAIM': 'jti',
    #
    # 'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    # 'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    # 'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}



# storage https://django-storages.readthedocs.io/en/latest/backends/gcloud.html
# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#     os.path.join(BASE_DIR, 'minfo-6b04e-63fe9a1abdd9.json')
# )
#
# DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# GS_BUCKET_NAME = 'minfo-6b04e.appspot.com'