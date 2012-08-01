from copy import deepcopy
from django.utils.translation import ugettext_lazy as _

from django.contrib import admin

from .models import MediaArtefact, Topic, Tag, GlossaryTerm

from mezzanine.core.admin import DisplayableAdmin


class MediaAdmin(DisplayableAdmin):
    fieldsets = (
                 (None, {
                         "fields": ["title", "media_type","thumbnail","embed_code","content","tags"],
                          }),
                 )


class TopicAdmin(DisplayableAdmin):
    fieldsets = (
        (None, {
            "fields": ["parent_topic","title","icon", "content","featured_media"],
        }),
    )
    
class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ["name","tag_type"],
        }),
    )
    
    
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