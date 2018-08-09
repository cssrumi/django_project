from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from products.forms import ProductForm
from products.models import Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'product/product_list.html'

    form_class = ProductForm

    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'product/product_list.html'

    form_class = ProductForm

    model = Product


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')
