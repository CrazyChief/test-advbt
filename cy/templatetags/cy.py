"""Template tags for Currency app"""
from django import template
from django.conf import settings
# from django.http import request
from ..models import Cy
from ..utils import get_active_currency, calc

register = template.Library()


class ChangeCurrencyNode(template.Node):

    def __init__(self, price, currency):
        self.price = template.Variable(price)
        self.currency = template.Variable(currency)

    def render(self, context):
        try:
            return calc(self.price.resolve(context), self.currency.resolve(context))
        except template.VariableDoesNotExist:
            return ''


@register.tag(name='change_currency')
def change_currency(parser, token):
    # print("Parser: %s" % parser)
    # print("Token: %s" % token)
    try:
        tag_name, current_price, new_currency = token.split_contents()
    except ValueError:
        tag_name = token.contents.split()[0]
        raise template.TemplateSyntaxError(
            """%r tag requires exactly two arguments""" % tag_name
        )
    print("curr_price: %s \t new_curr: %s" % (current_price, new_currency))
    return ChangeCurrencyNode(current_price, new_currency)


@register.tag('calc_cy')
def do_calc_cy(price):
    return price


@register.simple_tag(takes_context=True)
def curr_context(context):
    request = context['request']
    context['CURRENCIES'] = Cy.objects.filter(active=True)
    context['CURRENCY_ACTIVE'] = get_active_currency(request)
    return ''


