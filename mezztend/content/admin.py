from copy import deepcopy

from django.contrib import admin

from mezzanine.pages.admin import PageAdmin, page_fieldsets

from models import MODELS

if not MODELS or "contentblock" in MODELS:
    from models import ContentBlock
    
    class ContentBlockAdmin(admin.ModelAdmin):
        list_display = ('title', 'description', 'slug')
        fields = ('title', 'description', 'content', 'image', 'slug')
        readonly_fields = ('slug',)
    admin.site.register(ContentBlock, ContentBlockAdmin)
    
if not MODELS or "internallink" in MODELS:
    from models import InternalLink

    # Drop the meta data fields, and move slug towards the top.
    internal_link_fieldsets = deepcopy(page_fieldsets[:1])
    internal_link_fieldsets[0][1]["fields"] = internal_link_fieldsets[0][1]["fields"][:-1]
    
    class InternalLinkAdmin(PageAdmin):
        fieldsets = internal_link_fieldsets
    admin.site.register(InternalLink, InternalLinkAdmin)
    
if not MODELS or "menuitem" in MODELS:
    from models import MenuItem
    
    # Drop the meta data fields, and move slug towards the top.
    menu_item_fieldsets = deepcopy(page_fieldsets[:1])
    menu_item_fieldsets[0][1]["fields"] = menu_item_fieldsets[0][1]["fields"][:-1]
    menu_item_fieldsets[0][1]["fields"].insert(1, "slug")
    
    class MenuItemAdmin(PageAdmin):
        fieldsets = menu_item_fieldsets
    admin.site.register(MenuItem, MenuItemAdmin)

if not MODELS or "twocolumnrichtextpage" in MODELS:
    from models import TwoColumnRichTextPage
    
    admin.site.register(TwoColumnRichTextPage, PageAdmin)
