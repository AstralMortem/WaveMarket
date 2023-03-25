from django import forms
from account.models import Address


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input',
        'placeholder': 'Promo code',
    }))

class PaymentForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(widget=forms.EmailInput())


    class Meta:
        model = Address
        fields = ['first_name', 'last_name', 'email','country', 'state','city', 'street', 'build', 'zip']

