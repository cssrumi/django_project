from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from products.models import Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = ProductForm

    model = Product


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'product/product_list.html'

    form_class = ProductForm

    model = Product


class PostDeleteVied(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('post_list')