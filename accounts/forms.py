from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email','phone_number')

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email','phone_number', 'is_active')
