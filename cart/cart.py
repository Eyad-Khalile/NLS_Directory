from django.conf import settings
from map_app.models import Orgs
from django.db.models import Q
from django.contrib import messages


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, org):
        org_id = str(org.id)
        if org_id not in self.cart:
            self.cart[org_id] = {'name': str(
                org.name), 'level': str(org.level)}
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, org):
        org_id = str(org.id)
        if org_id in self.cart:
            del self.cart[org_id]
            self.save()


def clear(self):
    del self.session[settings.CART_SESSION_ID]
    self.save()
