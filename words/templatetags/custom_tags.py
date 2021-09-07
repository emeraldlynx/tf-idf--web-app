from django.template.defaulttags import register
from django import template


register = template.Library()

@register.filter
def get_item(dictionary: dict, key):
    try:
        return dictionary.get(key)
    except:
        print("Key", key)

register.filter('get_item', get_item)
