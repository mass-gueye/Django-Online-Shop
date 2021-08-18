from category.models import Category
from django.db import models
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(default="",null=False, unique=True) # new
    description = models.TextField(max_length=255, blank=True)
    price = models.FloatField(default=0.00)
    product_image = models.ImageField(upload_to='photos/products', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product-detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
    


