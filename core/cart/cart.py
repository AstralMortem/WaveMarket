from decimal import Decimal
from django.conf import settings
from shop.models import Item
from shop.models import Coupon
from django.contrib import messages
import json
from django.core.serializers.json import DjangoJSONEncoder

class Cart():

    def __init__(self, request):
        self.request = request
        self.session = self.request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
           cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.coupon_code = self.session.get('coupon')



    def add(self,item):
        product_id = str(item.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'price':str(item.price), 
                            'discount_price': str(item.discount_price)}
            messages.success(self.request, "Successfully added to cart")
        else:
            messages.info(self.request, "Item already in cart")
        self.save()
    
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
        

    def remove(self,item):
        product_id = str(item.id)
        if product_id in self.cart:
            del self.cart[product_id]
            messages.success(self.request, "Successfully removed from cart")
        else:
            messages.danger(self.request,"Not in cart")
        self.save()

    def clear(self):
       del self.session[settings.CART_SESSION_ID]
       if self.session.get('coupon', None):
           del self.session['coupon']
       messages.success(self.request, "Successfully cleared cart")
       self.session.modified = True

    def total(self):
        price = Decimal()
        for item in self.cart.values():
            if item['discount_price'] != "None":
                price += Decimal(item['discount_price'])
            else:
                price += Decimal(item['price'])
        if self.coupon:
            price -= self.coupon.amount
        if price <=0:
            price = Decimal(0)
        return price
    
    def __len__(self):
        return len(self.cart)
    
    def __iter__(self):
        product_ids = self.cart.keys()
        product = Item.objects.filter(id__in=product_ids)
        for item in product:
            yield item

    @property
    def coupon(self):
        if self.coupon_code:
            return Coupon.objects.get(code=self.coupon_code)
        return None