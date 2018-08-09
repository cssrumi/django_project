from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('add/', views.ProductCreateView.as_view(), name='product_create'),
    path('show/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
    path('providers/', views.ProviderListView.as_view(), name='provider_list'),
    path('providers/add/', views.ProviderCreateView.as_view(), name='provider_create'),
    path('providers/show/<int:pk>', views.ProviderDetailView.as_view(), name='provider_detail'),
    path('providers/edit/<int:pk>', views.ProviderUpdateView.as_view(), name='provider_update'),
    path('providers/delete/<int:pk>', views.ProviderDeleteView.as_view(), name='provider_delete'),
]
