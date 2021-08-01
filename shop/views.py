from django.db import models
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import DetailView
from store.models import Product

class HomeView(ListView):
    template_name = "index.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(is_available=True)
        return qs
    


