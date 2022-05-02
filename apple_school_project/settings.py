from apple_school_project.settings.base import *

ALLOWED_HOSTS = ["itsmekiran.com",
                 "www.itsmekiran.com", "https://www.itsmekiran.com"]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR) + '/templates/', ],
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

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = '/home3/kiranpau/itsmekiran.com/apple/static'

# Media Files
MEDIA_ROOT = '/home3/kiranpau/itsmekiran.com/apple/media'
MEDIA_URL = '/media/'
