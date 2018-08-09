from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('show/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('edit/<int:pk>', views.ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', views.ProductDeleteView.as_view(), name='product_delete'),
]
