from django.contrib import admin
from .models import Category
# Register your models here.
@admin.register(Category)
@admin.display(empty_value = '-empty-')
class CategoryAdmin(admin.ModelAdmin):
    # fields = ('category_name', 'description')
    # list_display = ('category_name', )
    # list_filter = ('category_name',)
    prepopulated_fields = {'slug': ('category_name',)} # new
