import django_filters
from .models import Item,Tag
from django import forms
from crispy_forms.helper import FormHelper
from django.db.models import Q
from decimal import Decimal




class ItemFilter(django_filters.FilterSet):
    helper = FormHelper()



    CHOICES = {
        ('ascending','Ascending'),
        ('descending','Descending'),
    }
   
    price__gt = django_filters.NumberFilter(method='filter_by_prices_gt', lookup_expr='gt',
    widget=forms.HiddenInput(attrs={'id': 'slider-min'}))
    price__lt = django_filters.NumberFilter(method='filter_by_prices_lt', lookup_expr='lt',
    widget=forms.HiddenInput(attrs={'id': 'slider-max'}))
    ordering = django_filters.ChoiceFilter(label='Ordering',choices=CHOICES, method='filter_by_order' )
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),label='Tags',field_name='tags',widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Item
        fields = ['ordering','tags']
        

    def filter_by_order(self,queryset,name,value):
        exp = 'created_at' if value == 'ascending' else '-created_at'
        return queryset.order_by(exp)

    def filter_by_prices_gt(self,queryset,name,value):

        qs = queryset.filter(
            Q(price__gt=value-1)|       # add +1/-1 cause Decimal lookup not show in__lookup in view so i inc/dec this value to get all ranfe of items
            Q(discount_price__gt=value-1)
        )
        return qs
    def filter_by_prices_lt(self,queryset,name,value):
        qs = queryset.filter(
            Q(price__lt=value+1)|
            Q(discount_price__lt=value+1)
        )
        return qs

    