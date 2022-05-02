from apple_school_project.settings.base import *

ALLOWED_HOSTS = ["*"]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates/', ],
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

# static files
STATICFILES_DIRS = [
        'static',
]

STATIC_URL = '/static/'

# Media Files
MEDIA_ROOT = 'media/'
MEDIA_URL = '/media/'
