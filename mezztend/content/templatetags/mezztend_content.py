
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

@register.as_tag
def load_content_blocks(slug, limit=3):
    return list(ContentBlock.objects.filter(slug__startswith=slug).order_by('slug')[:limit])
