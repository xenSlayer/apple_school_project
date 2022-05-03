from django.contrib import admin
from .models import TestimonialModel, NewsAnnouncementsModel, BlogModel, ContactUsModel, EventModel, DownloadsModel
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportActionModelAdmin


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', )


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', )


admin.site.register(NewsAnnouncementsModel, NewsAdmin)
admin.site.register(BlogModel, BlogAdmin)
admin.site.register(TestimonialModel)
admin.site.register(DownloadsModel)

@admin.register(EventModel)
class ViewAdmin(ImportExportActionModelAdmin):
    pass


@admin.register(ContactUsModel)
class ContactUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
