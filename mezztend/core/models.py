from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import RichTextField

class TwoColumnRichText(models.Model):
    """
    Provides Two Rich Text fields for managing general content and making
    it searchable.
    """

    left_column = RichTextField(_("Left column"))
    right_column = RichTextField(_("Right column"))

    search_fields = ("left_column", "right_column")

    class Meta:
        abstract = True