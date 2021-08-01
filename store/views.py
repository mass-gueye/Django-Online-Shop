from django.shortcuts import get_object_or_404
from category.models import Category
from django.views.generic.list import ListView
from django.views.generic import DetailView
from store.models import Product
# Create your views here.
class StoreView(ListView):
    template_name = "store.html"
    model = Product
    context_object_name = "products"
    
    def get_queryset(self):
        store_path = self.request.get_full_path()
        if store_path=='/store/':
            qs = super().get_queryset()
            qs = qs.filter(is_available =True)
            return qs
        else:
            category=get_object_or_404(Category,slug=self.kwargs['category_slug'])
            query_s = super().get_queryset()
            query_s = query_s.filter(is_available =True,category=category)
            return query_s
        
class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    model = Product

    def get_object(self, queryset=None):
        return Product.objects.get(slug=self.kwargs.get("product_slug"))

        
    



