from django.urls import path, include
from rest_framework import routers
from .views import index, about, MyFileView, facilities, events, contact, gallery, downloads, login
from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('facilities/', facilities, name='facilities'),
    path('events/', events, name='events'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contact, name='contact'),
    path('downloads/', downloads, name='downloads'),
    path('login/', login, name='login'),
    path('api/school/upload/', MyFileView.as_view(), name='file-upload'),
    path('summernote/', include('django_summernote.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
