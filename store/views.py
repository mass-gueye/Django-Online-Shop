from django.core import paginator
from django.http import request
from cart.models import CartItem
from django.shortcuts import get_object_or_404, render
from category.models import Category
from django.views.generic.list import ListView
from django.views.generic import DetailView
from store.models import Product

from cart.views import _cart_id
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.


class StoreView(ListView):
    template_name = "store.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        store_path = self.request.get_full_path()
        if store_path == '/store/':
            qs = super().get_queryset()
            qs = qs.filter(is_available=True).order_by('id')
            paginator = Paginator(qs, 6)
            page = self.request.GET.get('page')
            paged_product = paginator.get_page(page)
            return paged_product
        elif '/store/category/' in store_path:
            print(f"====${store_path}===")
            category = get_object_or_404(
                Category, slug=self.kwargs['category_slug'])
            query_s = super().get_queryset()
            query_s = query_s.filter(
                is_available=True, category=category).order_by('id')
            paginator = Paginator(query_s, 3)
            page = self.request.GET.get('page')
            paged_product = paginator.get_page(page)
            return paged_product

        else:
            query_s = super().get_queryset().order_by('id')
            paginator = Paginator(query_s, 3)
            page = self.request.GET.get('page')
            paged_product = paginator.get_page(page)
            return paged_product
    # def get_context_data(self, **kwargs):

    #     products=Product.objects.all().filter(is_available=True).order_by('id')
    #     paginator = Paginator(products,6)
    #     page = self.request.GET.get('page')
    #     paged_product = paginator.get_page(page)
    #     context = super().get_context_data(**kwargs)
    #     context["products"] = paged_product
    #     return context


class ProductDetailView(DetailView):
    template_name = "product_detail.html"
    model = Product

    def get_object(self, queryset=None):
        slug = Product.objects.get(slug=self.kwargs.get("product_slug"))
        return slug

    def get_context_data(self, **kwargs):
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(
            self.request), product=self.get_object()).exists()

        context = super().get_context_data(**kwargs)
        context["in_cart"] = in_cart
        return context



def search(request):
    template_name = "store.html"
    context={}
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products=Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            context['products'] =products
            print(f"================{products}")
    return render(request, template_name ,context)