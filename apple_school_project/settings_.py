from apple_school_project.settings.base import *

SECRET_KEY = '4n=@9*u$vk5icclq*j!r$cl+r77ct$&+=nrb&g#t6%(e$8&q2u'

ALLOWED_HOSTS = ["apple.itsmekiran.com", "https://apple.itsmekiran.com/"]

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
