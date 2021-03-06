from copy import deepcopy

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import RichText, Slugged
from mezzanine.pages.models import Page

from mezztend.core.models import TwoColumnRichText

class ContentBlock(RichText, Slugged):
    """
    Provides a block of rich text content which can be placed in a
    template using the associated render_content_block tag
    """
    description = models.CharField(max_length=100)
    image = FileField(upload_to="contentblocks", format="Image",
                      max_length=255, null=True, blank=True,
                      help_text="Optional, may be used in certain "
                                "circumstances and not others")
    href = models.CharField(max_length=500, blank=True,
        help_text="An optional link for the image or otherwise.")
    
    class Meta:
        db_table = "mezztend_content_contentblock"
    
    def __unicode__(self):
        return self.title


class MenuItem(Page):
    """
    A general content type for creating menu items which have no content
    associated with them.
    """
    href = models.CharField(max_length=500, blank=True,
        help_text="If blank this will simply sit in the menus, otherwise it will "
                  "link to whatever you specify here.")
    
    class Meta:
        db_table = "mezztend_content_menuitem"
        verbose_name = _("Menu item")
        verbose_name_plural = _("Menu items")

    def get_absolute_url(self):
        if self.href:
            return self.href
        return '#'

original_get_absolute_url = deepcopy(Page.get_absolute_url) 
def menu_item_get_absolute_url(self):
    """
    Returns a menu's href if this is a menu, otherwise, returns as normal
    """
    if self.content_model == "menuitem":
        return self.get_content_model().get_absolute_url()
    return original_get_absolute_url(self)
Page.get_absolute_url = menu_item_get_absolute_url

class TwoColumnRichTextPage(Page, TwoColumnRichText):
    """
    Implements a page with two Rich Text content fields
    """
    
    class Meta:
        db_table = "mezztend_content_twocolumnrichtextpage"
        verbose_name = _("Two column rich text page")
        verbose_name_plural = _("Two column rich text pages")
    
    