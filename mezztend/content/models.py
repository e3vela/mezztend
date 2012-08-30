from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.models import RichText, Slugged
from mezzanine.pages.models import Page

from mezztend.core.models import TwoColumnRichText

class ContentBlock(RichText, Slugged):
    """
    Provides a block of rich text content which can be placed in a
    template using the associated render_content_block tag
    """
    description = models.CharField(max_length=100)
    
    class Meta:
        db_table = "mezztend_content_contentblock"
    
    def __unicode__(self):
        return self.title

class TwoColumnRichTextPage(Page, TwoColumnRichText):
    """
    Implements a page with two Rich Text content fields
    """
    
    class Meta:
        db_table = "mezztend_content_twocolumnrichtextpage"
        verbose_name = _("Two column rich text page")
        verbose_name_plural = _("Two column rich text pages")
    
    