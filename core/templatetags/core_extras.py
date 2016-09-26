__author__ = 'User'

from django import template

register = template.Library()

@register.filter
def in_cart_session(code,cart):
    insession = False
    for item in cart:
        if item.id == code:
            insession = True
            break
    return insession

@register.filter
def split(price):
    str_price = str(price)
    return str_price[:-3]