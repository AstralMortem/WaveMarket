from django.shortcuts import render, get_object_or_404,redirect, HttpResponse
from django.views import generic
from shop.models import Item, Coupon, Order
from account.models import Customer, Address
from .forms import CouponForm, PaymentForm
from .cart import Cart
from django.contrib import messages
import json
from django.utils import timezone
from datetime import datetime
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django_htmx.http import HttpResponseClientRefresh
from wayforpay.wayforpay import WayForPayAPI, PaymentRequests
from django.contrib.sites.models import Site
from django.views.decorators.csrf import csrf_exempt


def cart_length(request):
    return render(request, "cart_length.html")

def cart_view(request, *args, **kwargs):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart, 'coupon':CouponForm()} )

def cart_add(request, items_id,*args, **kwargs):
    cart = Cart(request)
    item = get_object_or_404(Item, id=items_id)
    cart.add(item)
    response = render(request,'cart_table.html', {'cart': cart})
    response["HX-Trigger"] = json.dumps({'update-cart':'', 'message':''})
    return response

def cart_remove(request, items_id,*args, **kwargs):
    cart = Cart(request)
    item = get_object_or_404(Item, id=items_id)
    cart.remove(item)
    response = render(request,'cart_table.html', {'cart': cart})
    response["HX-Trigger"] = json.dumps({'update-cart':'', 'message':''})
    return response

def coupon_add(request):
    if request.method == 'POST':
        form = CouponForm(request.POST)
        if form.is_valid():
            coupon_code = form.cleaned_data['code']
            session_coupon = request.session.get('coupon', None)
            if session_coupon:
                messages.info(request, "Coupon already used")
            else:
                try:
                    coupon = Coupon.objects.get(code=coupon_code)
                    request.session['coupon'] = coupon_code
                    request.session.modified = True
                    messages.success(request, "Coupon successfully added")
                except:
                    messages.error(request, "Coupon does not exist")

            cart = Cart(request)
            response = render(request,'cart_table.html', {'cart': cart})
            response["HX-Trigger"] = 'message'
            return response
        
def coupon_remove(request):
    
    session_coupon = request.session.get('coupon', None)
    if session_coupon:
        del request.session['coupon']
        request.session.modified = True
        messages.success(request, 'Coupon removed successfully')
    else:
        messages.error(request, 'Coupon does not exist')
    cart = Cart(request)
    response = render(request,'cart_table.html', {'cart': cart})
    response["HX-Trigger"] = 'message'
    return response

def delete_order(request,id):
    order = Order.objects.get(id=id)
    if order.ordered == False:
        order.delete()
        messages.success(request, 'Order deleted successfully')
    response = redirect('account:orders')
    response["HX-Trigger"] = 'message'
    return response



@csrf_exempt
@login_required(login_url="account:login")
def payment_view(request):
    if request.user.address:
        last_order = Order.objects.filter(user=request.user)
        cart = Cart(request)
        names = []
        cost = []
        amount = []
        site = Site.objects.get_current()
    
        if last_order.count() <= 0 or last_order[0].ordered:
            order = Order(
                user = request.user,
                ordered_date = timezone.now(),
                coupon = cart.coupon
            )
            order.save()
            for item in Item.objects.filter(id__in=cart.cart.keys()):
                names.append(item.name)
                cost.append(str(item.get_final_price()))
                amount.append("1")
                order.items.add(item)
            order.save()
            

            data = {
            'orderReference': str(order.id),
            'orderDate': int(round(order.ordered_date.timestamp())),
            'amount': str(order.get_total()),
            'currency': 'USD',
            'productPrice': cost,
            'productName': names,
            'serviceUrl': site.domain + '/cart/payment-service/',
            'returnUrl': site.domain + '/cart/payment-finish/',
            'productCount': amount,
            'straightWidget': 'true',
            'language': 'EN'
        }
        else:
            for item in Item.objects.filter(id__in=cart.cart.keys()):
                names.append(item.name)
                cost.append(str(item.get_final_price()))
                amount.append("1")
                last_order[0].items.add(item)
            last_order[0].coupon = cart.coupon
            last_order[0].save()
            data = {
            'orderReference': str(last_order[0].id),
            'orderDate': int(round(last_order[0].ordered_date.timestamp())),
            'amount': str(last_order[0].get_total()),
            'currency': 'USD',
            'productPrice': cost,
            'productName': names,
            'serviceUrl': site.domain + '/cart/payment-service/',
            'returnUrl': site.domain + '/cart/payment-finish/',
            'productCount': amount,
            'straightWidget': 'true',
            'language': 'EN'
        }
        wp = WayForPayAPI(merchant_account=settings.WAYFORPAY_ACCOUNT,
                          merchant_key=settings.WAYFORPAY_KEY,
                          merchant_domain=site.domain)
        

        widget = PaymentRequests(merchant_account=settings.WAYFORPAY_ACCOUNT,
                          merchant_key=settings.WAYFORPAY_KEY,
                          merchant_domain=site.domain)
        widget = widget.generateForm(data)
        cart = Cart(request)
        cart.clear()
        return render(request, 'wayforpaywidget.html', {'widget': widget})
    else:
        messages.error(request, 'Please add an address first')
        response = render(request,'payment.html')
        response["HX-Trigger"] = 'message'
        return response

@csrf_exempt
def payment_finish(request):
    answer = request.POST
    order_id = answer.get('orderReference', None)
    status = answer.get('transactionStatus',None)
    if status and status == "Approved":
        order = Order.objects.get(id=order_id)
        order.ordered = True
        order.save()
        messages.success(request, 'Payment successful')
        response = render(request, 'success_pay.html', {'order': order})
        response['HX-Trigger'] = 'message'
        return response
    else:
        messages.error(request, 'Payment UNsuccessful')
        response = HttpResponse("Error")
        response['HX-Trigger'] = 'message'
        return response

@csrf_exempt
def payment_service(request):
    return HttpResponse()