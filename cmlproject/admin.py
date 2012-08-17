from copy import deepcopy
from django.utils.translation import ugettext_lazy as _

from django.contrib import admin

from .models import MediaArtefact, Topic, Tag, GlossaryTerm

from mezzanine.core.admin import DisplayableAdmin


class MediaAdmin(DisplayableAdmin):
    fieldsets = (
                 (None, {
                         "fields": ["title", "media_url","content","tags"],
                          }),
                 )
    
    list_display = ("title", "media_url", "status")
    list_filter = ('tags', 'featured_in')
    date_hierarchy = ""


class TopicAdmin(DisplayableAdmin):
    fieldsets = (
        (None, {
            "fields": ["parent_topic","title","related_tag","icon", "content","featured_media"],
        }),
    )
    
    
class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ["name","tag_type"],
        }),
    )
    
    list_display = ("name","tag_type")
    
    
class GlossaryTermAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ["name","explanation"],
        }),
    )


admin.site.register(Topic, TopicAdmin)
admin.site.register(MediaArtefact,MediaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(GlossaryTerm, GlossaryTermAdmin)