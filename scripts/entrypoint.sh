#!/bin/sh

set -e

export DJANGO_SETTINGS_MODULE=apple_school_project.settings.production

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module apple_school_project.wsgi