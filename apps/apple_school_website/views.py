from django.template.response import TemplateResponse
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.apple_school_website.serializers import TestimonialSerializer, NewsAnnouncementsSerializer, MyFileSerializer, \
    BlogSerializer, ContactUsSerializer, EventSerializer
from .models import DownloadsModel, TestimonialModel, NewsAnnouncementsModel, BlogModel, ContactUsModel, EventModel


# Pagination class
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


# Retrieve testimonials
class TestimonialView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = TestimonialModel.objects.all()
    serializer_class = TestimonialSerializer


# Retrieve latest news and announcements
class NewsAnnouncementsView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = NewsAnnouncementsModel.objects.all().order_by('-date_created')
    serializer_class = NewsAnnouncementsSerializer


# Retrieve files
class MyFileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = MyFileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Retrieve Blog
class BlogView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = BlogModel.objects.all().order_by('-date_created')
    serializer_class = BlogSerializer


# Retrieve Contact us
class ContactUsView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = ContactUsModel.objects.all().order_by('-date_created')
    serializer_class = ContactUsSerializer


# Retrieve Event
class EventView(viewsets.ModelViewSet):
    pagination_class = StandardResultsSetPagination
    queryset = EventModel.objects.all().order_by('-event_date')
    serializer_class = EventSerializer


# Renders React's index page
def index(request):
    testimonials = TestimonialModel.objects.all()
    return TemplateResponse(request, 'apple/index.html', context={
        "testimonials": testimonials,
    })


def about(request):
    return TemplateResponse(request, 'apple/about.html', context={})


def facilities(request):
    return TemplateResponse(request, 'apple/facilities.html', context={})


def events(request):
    events = EventModel.objects.all()
    return TemplateResponse(request, 'apple/events.html', context={
        "events": events
    })


def gallery(request):
    return TemplateResponse(request, 'apple/gallery.html', context={})


def contact(request):
    return TemplateResponse(request, 'apple/contact.html', context={})


def downloads(request):
    downloads = DownloadsModel.objects.all()
    return TemplateResponse(request, 'apple/downloads.html', context={
        "downloads": downloads
    })


def login(request):
    return TemplateResponse(request, 'apple/login.html', context={})
