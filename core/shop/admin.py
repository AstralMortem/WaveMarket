from django.contrib import admin
from .models import *
# Register your models here.



class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['name']}


admin.site.register(Item,ItemAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(AudioFragment)
admin.site.register(Order)
admin.site.register(Coupon)