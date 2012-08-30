
from mezzanine import template

from mezztend.content.models import ContentBlock

register = template.Library()

@register.as_tag
def render_content_block(slug):
    try:
        cb = ContentBlock.objects.get(slug=slug)
    except ContentBlock.DoesNotExist:
        cb = None
    return cb