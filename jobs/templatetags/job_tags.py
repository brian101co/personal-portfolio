from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(name="anchor")
def route_to_page_anchor(url_name, section_id):
    return reverse(url_name) + '#' + section_id
