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

@register.filter
def next_el(some_list, current_index):
    """
    Returns the next element of the list using the current index if it exists.
    Otherwise returns an empty string.
    """
    try:
        return some_list[int(current_index) + 1] # access the next element
    except:
        return '' # return empty string in case of exception