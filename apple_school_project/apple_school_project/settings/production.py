from apple_school_project.settings.base import *
import os

with open('/app/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('POSTGRES_NAME'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'HOST': 'db',
#         'PORT': 5432,
#     }
# }

DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = []
ALLOWED_HOSTS += os.environ.get("ALLOWED_HOSTS", "").split(",")

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

STATIC_ROOT = '/vol/web/static'
MEDIA_ROOT = '/vol/web/media'
