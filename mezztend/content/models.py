from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import RichText, Slugged
from mezzanine.pages.models import Page

from mezztend.core.models import TwoColumnRichText

if "contentblock" in settings.MEZZTEND_CONTENT_MODELS:
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

if "menuitem" in settings.MEZZTEND_CONTENT_MODELS:
    class MenuItem(Page):
        """
        A general content type for creating menu items which have no content
        associated with them.
        """
    
        class Meta:
            verbose_name = _("Menu item")
            verbose_name_plural = _("Menu items")
    
        def get_absolute_url(self):
            return '#'

if "twocolumnrichtextpage" in settings.MEZZTEND_CONTENT_MODELS:
    class TwoColumnRichTextPage(Page, TwoColumnRichText):
        """
        Implements a page with two Rich Text content fields
        """
        
        class Meta:
            db_table = "mezztend_content_twocolumnrichtextpage"
            verbose_name = _("Two column rich text page")
            verbose_name_plural = _("Two column rich text pages")
    
    