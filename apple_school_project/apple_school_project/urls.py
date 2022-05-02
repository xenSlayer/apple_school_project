from django.contrib import admin
from django.urls import path, include

from apple_school_website import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
]
