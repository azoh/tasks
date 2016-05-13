from django import template

register = template.Library()

@register.filter(name='get_age')
def get_age(value):

    if value > 13:
        return "allowed!"
    else:
        return "blocked!"
