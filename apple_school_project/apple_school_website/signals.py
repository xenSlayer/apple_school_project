from django.db.models.signals import pre_save
from django.dispatch import receiver
from apple_school_website.models import NewsAnnouncementsModel, BlogModel


@receiver(pre_save, sender=NewsAnnouncementsModel)
def remove_slash_news(sender, instance, **kwargs):
    instance.description = instance.description.replace("\"", "\'")


@receiver(pre_save, sender=BlogModel)
def remove_slash_blog(sender, instance, **kwargs):
    instance.description = instance.description.replace("\"", "\'")
