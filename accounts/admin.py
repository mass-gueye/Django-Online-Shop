from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import UserForm, UserChangeForm
# Register your models here.
@admin.register(User)
@admin.display(empty_value = '-empty-')

class UserAdmin(UserAdmin):
    add_form = UserForm
    form = UserChangeForm
    model = User

    list_display = ['email', 'username','phone_number','is_active',]
    list_display_links=('email','username')
    