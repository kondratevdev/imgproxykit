from django import template

from imgproxykit.integrations.django.shortcuts import (
    imgproxy_url,
    imgproxy_variants,
)

register = template.Library()

# Keep URL generation shared with Python callers; simple_tag handles escaping.
register.simple_tag(imgproxy_url)
register.simple_tag(imgproxy_variants)
