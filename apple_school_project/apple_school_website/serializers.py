from rest_framework import serializers
from .models import TestimonialModel, NewsAnnouncementsModel, FileUploadModel, BlogModel, \
    ContactUsModel, EventModel


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestimonialModel
        fields = '__all__'


class NewsAnnouncementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsAnnouncementsModel
        fields = '__all__'


class MyFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploadModel
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsModel
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = '__all__'
