from django import template

register = template.Library()

@register.filter(name='specialChars')
def special_chars(url):
    return url.replace('%23', '#')