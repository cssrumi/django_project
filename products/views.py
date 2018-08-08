from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
