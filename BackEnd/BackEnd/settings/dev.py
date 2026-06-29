# myproject/settings/dev.py
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Simple SQLite for development
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'khiem_bui_blog',
        'USER':'postgres',
        'PASSWORD':'01636462128k',
        'HOST':'localhost',
        'PORT':'5432',
        'ATOMIC_REQUESTS': True,
        'TIME_ZONE': 'UTC',
        'CONN_HEALTH_CHECKS': False,
        'CONN_MAX_AGE': 0,
        "TIME_ZONE": "UTC", 
    }
}

INTERNAL_IPS = ['127.0.0.1']

STATIC_URL = 'static/'