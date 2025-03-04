from django.contrib import admin
from .models import *

class AllProductAdmin(admin.ModelAdmin):
    list_display = ['user','product_name','product_price','product_status']
    list_filter = ['user']

class Sell_BuyAdmin(admin.ModelAdmin):
    list_display = ['user','product','product_user']
    list_filter = ['user']

    def product_user(obj,user):
        return user.product.user


admin.site.register(AllProduct,AllProductAdmin)
admin.site.register(Status)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Sell_Buy,Sell_BuyAdmin)
admin.site.register(Provinces)
# Register your models here.
