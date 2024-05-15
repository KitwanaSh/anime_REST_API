from datetime import timedelta
import os
from pathlib import Path
# from decouple import config
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=lcfn^lrqa8ky^y-dr^!(%fd9+s8&(y_5nfb)^+nc7bfcad!-!'

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

    # third party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'djoser',
    'drf_spectacular',
    'django_filters',
    'django_celery_beat',
    'django_celery_results',
    'django_sonar',
    
    # Core apps
    'users',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'anime_RestAPI.urls'

AUTH_USER_MODEL = 'core.CustomUser'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'anime_RestAPI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'animedb',
        'USER': 'postgres',
        'PASSWORD': 'eze31',
        'HOST': 'localhost',
        'PORT': '5432',
   }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DJANGO_SONAR = {
    'excludes': [
        STATIC_URL,
        MEDIA_URL,
        '/sonar/',
        '/admin/',
        '/__reload__/',
    ],
}

# DJOSER SETTINGS
DJOSER = {
    'SERIALIZERS': {
        'user_create': 'users.serializers.UserCreateSerializer',
        'current_user': 'users.serializers.CurrentUserSerializer',
    }
}

# RESTFRAMEWORK SETTINGS
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
}


# API Docs settings
SPECTACULAR_SETTINGS = {
    'TITLE': 'Atsuko CLone API',
    'DESCRIPTION': 'Atsuko Clone project API Documents',
    'VERSION': '1.0.0',
    'SCHEMA_PATH_PREFIX': '/backend/api/*',
    # 'SERVE_PERMISSIONS': ['rest_framework.permissions.IsAuthenticated'],
    'DISABLE_ERRORS_AND_WARNINGS': True,
    'COMPONENT_SPLIT_REQUEST': True
}

BASE_BACKEND_URL = 'http://localhost:8000'

# GOOGLE AUTH SETTINGS
GOOGLE_OAUTH2_CLIENT_ID = os.getenv('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH2_CLIENT_SECRET')
GOOGLE_OAUTH2_PROJECT_ID = os.environ.get('GOOGLE_OAUTH2_PROJECT_ID')

# EMAIL SETTINGS
EMAIL_HOST_USER = os.getenv('SENDER_EMAIL')
EMAIL_HOST_PASSWORD = os.getenv('SENDER_EMAIL_PASSWORD')

# Celery settings
CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Africa/Accra'
CELERY_RESULT_BACKEND = 'django-db'

# Celery beat settings
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'