from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
@admin.display(empty_value = '-empty-')

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)} # new
    list_display = ["product_name","category","is_available","stock",]
    list_filter = ["category",]
