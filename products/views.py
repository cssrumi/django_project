from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.db.models import Q

from products.forms import ProductForm, ProviderForm
from products.models import Product, Provider


# Create your views here.

###########
# PRODUCT #
###########

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




############
# PROVIDER #
############

class ProviderListView(ListView):
    model = Provider
    queryset = Provider.objects.all()


class ProviderDetailView(DetailView):
    model = Provider


class ProviderCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'product/provider_list.html'

    form_class = ProviderForm

    model = Provider


class ProviderUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'product/provider_list.html'

    form_class = ProviderForm

    model = Provider


class ProviderDeleteView(LoginRequiredMixin, DeleteView):
    model = Provider
    success_url = reverse_lazy('products:provider_list')


@login_required
def search(request):
    template = 'products/search_results.html'

    query = request.GET.get('q')
    product_list = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    privider_list = Provider.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'products': product_list,
        'providers': privider_list,
    }
    return render(request, template, context)
