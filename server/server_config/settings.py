# server_config/settings.py

import os
from server_config.base_settings import *

# -------------------------------------------------------
# Debug & Hosts
# -------------------------------------------------------

DEBUG = False  # Mets True si tu développes en local
ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # À modifier en production

# -------------------------------------------------------
# Celery Configuration
# -------------------------------------------------------

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "amqp://guest:guest@rabbitmq:5672//")
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"

# -------------------------------------------------------
# Installed Apps
# -------------------------------------------------------

INSTALLED_APPS += [
    'django_prometheus',
    'django_celery_results',
    'django_celery_beat',
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

