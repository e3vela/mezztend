from copy import deepcopy

from django.contrib import admin

from mezzanine.pages.admin import PageAdmin, page_fieldsets

from models import MODELS

if "contentblock" in MODELS:
    from models import ContentBlock
if "menuitem" in MODELS:
    from models import MenuItem
if "twocolumnrichtextpage" in MODELS:
    from models import TwoColumnRichTextPage

class ContentBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug')
    fields = ('title', 'description', 'content', 'image', 'slug')
    readonly_fields = ('slug',)


# Drop the meta data fields, and move slug towards the stop.
menu_item_fieldsets = deepcopy(page_fieldsets[:1])
menu_item_fieldsets[0][1]["fields"] = menu_item_fieldsets[0][1]["fields"][:-1]
menu_item_fieldsets[0][1]["fields"].insert(1, "slug")


class MenuItemAdmin(PageAdmin):

    fieldsets = menu_item_fieldsets

if "contentblock" in MODELS:
    admin.site.register(ContentBlock, ContentBlockAdmin)
if "menuitem" in MODELS:
    admin.site.register(MenuItem, MenuItemAdmin)
if "twocolumnrichtextpage" in MODELS:
    admin.site.register(TwoColumnRichTextPage, PageAdmin)
