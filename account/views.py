from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import SignUpForm, AddressForm, SetupForm
from .models import Address, Customer
from shop.models import Order, Item
from django.middleware.csrf import get_token
import os
from django.contrib.auth.decorators import login_required

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('account:login')

    def get_context_data(self, *args, **kwargs):
        context = super(UserRegisterView, self).get_context_data(*args, **kwargs)
        context['title'] = 'Sign Up | WaveMarket'
        return context

    def form_valid(self, form):
        user = form.save() #save the user
        return HttpResponseRedirect(self.success_url)


def user_setup_update(request):
    if request.method == 'POST':
        form = SetupForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return render(request, 'user_settings_card.html')
        else:
            render(request, 'user_card_actions.html', {'form': form})
    return render(request, 'user_card_actions.html', {'form': SetupForm(instance=request.user)})
    
@login_required
def profile_view(request, *args, **kwargs):
    order = Order.objects.filter(user=request.user)
    total = 0
    count = 0
    for i in order:
        total += i.get_price_in_items()
        count += i.get_count()
    dict= {'length':count, 'total':total}
    return render(request, 'profile.html', {'orders':dict, 'title': 'Profile | WaveMarket'})

def add_address(request, *args, **kwargs):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            request.user.address = form.instance
            request.user.save()
            return render(request, 'address_card.html')
    return render(request, 'address_card_actions.html', {'form': AddressForm()})

def update_address(request, id):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'address_card.html')
    return render(request, 'address_card_actions.html', {'form': AddressForm(instance=request.user.address)})

def delete_address(request, id):
    address = Address.objects.get(id=id)
    address.delete()
    return render(request, 'address_card.html')

@login_required
def order_view(request):
    items = Order.objects.filter(user=request.user)
    return render(request, 'user_orders.html', {'items':items, 'title': 'Orders | WaveMarket' })

