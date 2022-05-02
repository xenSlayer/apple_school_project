from apple_school_project.settings.base import *


STATIC_URL = '/static/'

# STATIC_ROOT = '/home3/kiranpau/itsmekiran.com/apple/static'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    '/home3/kiranpau/itsmekiran.com/apple/static'
)

# Media Files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
