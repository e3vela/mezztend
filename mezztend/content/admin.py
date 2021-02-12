from copy import deepcopy

from django.contrib import admin

from mezzanine.pages.admin import PageAdmin, page_fieldsets
from mezzanine.pages.models import Link

from models import ContentBlock, MenuItem, TwoColumnRichTextPage


@admin.register(ContentBlock)
class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    fields = ('title', 'description', 'content', 'image', 'href', 'slug')
    readonly_fields = ('slug',)


# Drop the meta data fields, and move slug towards the top.
menu_item_fieldsets = deepcopy(page_fieldsets[:1])
menu_item_fieldsets[0][1]["fields"] = menu_item_fieldsets[0][1]["fields"][:-1]
menu_item_fieldsets[0][1]["fields"].insert(1, "href")
menu_item_fieldsets[0][1]["fields"].insert(-1, "slug")


@admin.register(MenuItem)
class MenuItemAdmin(PageAdmin):
    fieldsets = menu_item_fieldsets


admin.site.register(TwoColumnRichTextPage, PageAdmin)
# menu item is more flexible
admin.site.unregister(Link)
