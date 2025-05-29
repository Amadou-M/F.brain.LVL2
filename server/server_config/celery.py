# server_config/celery.py

import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server_config.settings")

app = Celery("server")

# Charge les settings de Django à partir des variables CELERY_*
app.config_from_object("django.conf:settings", namespace="CELERY")

# Recherche automatiquement les tâches asynchrones dans les apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
