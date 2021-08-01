from django.shortcuts import render

# Create your views here.
# from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import UserForm

class SignUpView(CreateView):
    form_class = UserForm
    # success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'