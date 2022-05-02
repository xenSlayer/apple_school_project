from django.db import models
from apple_school_project import settings as setting


# Testimonial Model
class TestimonialModel(models.Model):
    name = models.CharField(max_length=100)
    relationToSchool = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.relationToSchool


# News and Announcements Model
class NewsAnnouncementsModel(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'News & announcement'
        verbose_name_plural = 'News & announcements'

    def __str__(self):
        return self.title


# File Upload Model
class FileUploadModel(models.Model):
    file = models.FileField(blank=False, null=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)


# Blog Model
class BlogModel(models.Model):
    title = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    BLOG_FROM = (
        ("Teacher", "Teacher"),
        ("Student", "Student"),
        ("Principal", "Principal"),
    )
    blog_from = models.CharField(choices=BLOG_FROM, max_length=20, default="Teacher")
    author_name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.title


# Contact us model
class ContactUsModel(models.Model):
    full_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    contact_number = models.CharField(max_length=30)
    message = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        return self.full_name


# Event date model
class EventModel(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return self.event_name

