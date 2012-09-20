from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import RichText, Slugged
from mezzanine.pages.models import Page

from mezztend.core.models import TwoColumnRichText

try:
    MODELS = settings.MEZZTEND_CONTENT_MODELS
except AttributeError:
    MODELS = None

if not MODELS or "contentblock" in MODELS:
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
        
        class Meta:
            db_table = "mezztend_content_contentblock"
        
        def __unicode__(self):
            return self.title

if not MODELS or "menuitem" in MODELS:
    class MenuItem(Page):
        """
        A general content type for creating menu items which have no content
        associated with them.
        """
        href = models.CharField(max_length=500, blank=True,
            help_text="If blank this will simply sit in the menus, otherwise it will "
                      "link to whatever you specify here.")
        
        class Meta:
            db_table = "mezztend_content_contentblock"
            verbose_name = _("Menu item")
            verbose_name_plural = _("Menu items")
    
        def get_absolute_url(self):
            if self.href:
                return self.href
            return '#'

if not MODELS or "twocolumnrichtextpage" in MODELS:
    class TwoColumnRichTextPage(Page, TwoColumnRichText):
        """
        Implements a page with two Rich Text content fields
        """
        
        class Meta:
            db_table = "mezztend_content_twocolumnrichtextpage"
            verbose_name = _("Two column rich text page")
            verbose_name_plural = _("Two column rich text pages")
    
    