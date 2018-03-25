from django import template
#from django.template.defaulttags import register

register = template.Library()


@register.filter
def lookup(value, key):
    return value.get(key, [])


@register.filter
def req_filter(string):
    return string.replace(',', '+')


@register.filter
def return_item(l, i):
    try:
        return l[i]
    except:
        return None


#@register.filter(name='lookup')
#def cut(value, arg):
#    return value[arg]