from django import template

register = template.Library()

@register.filter(name='get_bizzfuzz')
def get_bizzfuzz(value):

    if value % 5 == 0 and value % 3 == 0 :
        return "BizzFuzz"
    else:
        if value % 5 == 0:
            return "Fuzz"
        elif value % 3 == 0:
            return "Bizz"
        else:
            return value
