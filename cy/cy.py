from django.conf import settings
from .models import Cy


session_key = getattr(settings, 'CURRENCY_SESSION_KEY', 'currency')


class CY(object):
    base_currency = None
    # current_currency = None

    def __init__(self, request):
        self.request = request
        session_data = request.session.setdefault(session_key, {})
        session_item = session_data.setdefault('item', {})
        if not session_item:
            print("session_item is empty")
            session_item = self.set_currency(session_item)
        else:
            print("session_item is full")
        print(session_item)

        # self.session = self.request.session
        # cy = self.session.get(settings.CURRENCY_ID)
        # if not cy:
        #     cy = self.session[settings.CURRENCY_ID] = {}
        # self.cy = cy
        # print(self.cy)

        # print(session_key)
        # print(session_data)
        # print(session_item)

        # print(self.session)

    def get_base_currency(self):
        if self.base_currency is None:
            self.base_currency = Currency.objects.get(base=True)
        return self.base_currency

    # def get_currency(self, current_currency=None):
    #     if current_currency is None:
    #         self.current_currency = self.get_base_currency
    #     else:
    #         # pass
    #         current_currency = Currency.active
    #     self.current_currency = current_currency
    #     return self.current_currency

    def set_currency(self, session_item):
        if session_item is None:
            session_item['item'] = self.get_base_currency()
        # item = list(self.session_item.keys())
        # print(item)
        # print(session_item)
        return session_item