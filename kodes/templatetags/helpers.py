import re, locale

from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
def formatoNumero(value): 
    locale.setlocale(locale.LC_ALL, 'de_DE.utf-8')
    valor = locale.format('%.2f', value, grouping=True, monetary=True)
    #valor = '{:,}'.format(value).replace(',','.')
    return valor

@register.filter
def formatoNumeroPunto(value): 
    valor = '{:,}'.format(value).replace(',','.')
    return valor


@register.filter
def negate(boolean):
    return (not boolean).__str__()

