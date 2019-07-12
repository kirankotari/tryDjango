from django import template

register = template.Library()


@register.filter
def space_underscore(value):
    return value.replace(' ', '_')


@register.filter
def index(value, args):
    return value[args]
