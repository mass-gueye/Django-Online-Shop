from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
@admin.register(Cart, CartItem)
@admin.display(empty_value = '-empty-')
class CartAdmin(admin.ModelAdmin):
    list_display = ["cart_id",]

class CartItemAdmin(admin.ModelAdmin):
    list_display_links = ["product","cart","quantity",]
    list_filter = ["product","cart","quantity", "is_active",]
