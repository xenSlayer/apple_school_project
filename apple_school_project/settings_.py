from apple_school_project.settings.base import *

SECRET_KEY = '4n=@9*u$vk5icclq*j!r$cl+r77ct$&+=nrb&g#t6%(e$8&q2u'

ALLOWED_HOSTS = ["apple.itsmekiran.com", "https://apple.itsmekiran.com/", "*"]


# Change this later
cpanel_user = 'kiranpau'
domain = 'itsmekiran.com'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [f'/home3/{cpanel_user}/{domain}/apple/templates', ],
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
STATIC_ROOT = f'/home3/{cpanel_user}/{domain}/apple/static'

# Media Files
MEDIA_ROOT = f'/home3/{cpanel_user}/{domain}/apple/media'
MEDIA_URL = '/media/'
