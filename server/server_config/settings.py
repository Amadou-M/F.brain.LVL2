import os
from pathlib import Path
from server_config.base_settings import *

# -------------------------------------------------------
# Path Configuration
# -------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
# -------------------------------------------------------
# Debug & Hosts
# -------------------------------------------------------
DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# -------------------------------------------------------
# Application Definition
# -------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Vos applications personnalisées
    # ...
    
    # Applications tierces
    'django_prometheus',
    'django_celery_results',
    'django_celery_beat',
]

# -------------------------------------------------------
# Middleware Configuration
# -------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------------------------------
# Templates Configuration
# -------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# -------------------------------------------------------
# Database Configuration
# -------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'devops_db'),
        'USER': os.getenv('POSTGRES_USER', 'devops_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'devops_pass'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': 5432,
    }
}

# -------------------------------------------------------
# Celery Configuration
# -------------------------------------------------------
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@rabbitmq:5672//")
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# -------------------------------------------------------
# Static Files Configuration
# -------------------------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# -------------------------------------------------------
# Authentication & URLs
# -------------------------------------------------------
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

ROOT_URLCONF = 'server_config.urls'
WSGI_APPLICATION = 'server_config.wsgi.application'

# -------------------------------------------------------
# Internationalization
# -------------------------------------------------------
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True