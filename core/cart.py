__author__ = 'wanyama'

import datetime
import models

CART_ID = 'CART-ID'

class ItemAlreadyExists(Exception):
    pass

class ItemDoesNotExist(Exception):
    pass

class Cart:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = models.Cart.objects.get(id=cart_id,checked_out=False)
            except models.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.cartitem_set.all():
            yield item

    def new(self, request):
        cart = models.Cart(creation_date=datetime.datetime.now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, menu_item, unit_price, quantity=1):
        try:
            cart_item = models.CartItem.objects.get(
                cart=self.cart,
                menu_item=menu_item,
            )
        except models.CartItem.DoesNotExist:
            new_cart_item = models.CartItem()
            new_cart_item.cart = self.cart
            new_cart_item.menu_item = menu_item
            new_cart_item.unit_price = unit_price
            new_cart_item.quantity = quantity
            new_cart_item.save()
        else: #ItemAlreadyExists
            cart_item.unit_price = unit_price
            cart_item.quantity = cart_item.quantity + int(quantity)
            cart_item.save()

    def remove(self, menu_item):
        try:
            item = models.CartItem.objects.get(
                cart=self.cart,
                menu_item=menu_item,
            )
        except models.CartItem.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()


    def update(self, product, quantity, unit_price=None):
        try:
            item = models.CartItem.objects.get(
                cart=self.cart,
                menu_item=product,
            )
        except models.CartItem.DoesNotExist:
            raise ItemDoesNotExist
        else: #ItemAlreadyExists
            if quantity == 0:
                item.delete()
            else:
                item.unit_price = unit_price
                item.quantity = int(quantity)
                item.save()

    def count(self):
        result = 0
        for item in self.cart.cartitem_set.all():
            result += 1 * item.quantity
        return result

    def summary(self):
        result = 0
        for item in self.cart.cartitem_set.all():
            result += item.unit_price*item.quantity
        return result

    def clear(self):
        for item in self.cart.cartitem_set.all():
            item.delete()

    def delivery_fee(self):
        if self.cart.self_collect:
            return 0
        else:
            if self.count() == 0:
                return 0;
            elif self.count() <= 5 :
                return 5000
            elif self.count() <= 10:
                return 10000
            elif self.count() <= 15:
                return 15000
            else:
                return 15000

    def grand_total(self):
        total= self.summary()+self.delivery_fee()
        return total
