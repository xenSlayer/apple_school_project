from apple_school_project.settings.base import *
import os


SECRET_KEY = "hjf$b1!9#!i14i7jc7kn7dsne4st_c-qj0uh!bivpr+mj%7)gh"

DEBUG = bool(int(os.environ.get('DEBUG', "1")))

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(BASE_DIR, 'static/apple/')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Media Files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
