from django import template

register = template.Library()

@register.filter(name='make_list')
def make_list(value):
    return range(value)
