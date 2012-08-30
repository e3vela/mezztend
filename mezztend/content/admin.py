from django.contrib import admin

from mezzanine.pages.admin import PageAdmin

from models import ContentBlock, TwoColumnRichTextPage

class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    fields = ('title', 'description', 'content', 'slug')
    readonly_fields = ('slug',)


admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(TwoColumnRichTextPage, PageAdmin)
