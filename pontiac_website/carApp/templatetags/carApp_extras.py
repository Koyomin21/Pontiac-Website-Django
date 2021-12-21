from django import template

register = template.Library()

@register.filter(name="indexes", is_safe=True)
def get_slice_indexes(row):
    start = row*3
    end = row*3+3

    return str(start)+":"+str(end)