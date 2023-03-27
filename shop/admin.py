from django.contrib import admin
from .models import *
# Register your models here.



class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['name']}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['name']}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ['name']}


admin.site.register(Item,ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Order)
admin.site.register(Coupon)