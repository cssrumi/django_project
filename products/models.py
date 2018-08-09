from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.

class Provider(models.Model):
    name = models.CharField(max_length=120, null=False)
    description = models.TextField(max_length=500, null=True)
    location = models.CharField(max_length=100, null=False)

    def get_absolute_url(self):
        return reverse('products:provider_detail', kwargs={'pk': self.pk})

    def offer(self):
        return self.products

    def __str__(self):
        return self.name


class Product(models.Model):
    provider = models.ForeignKey('products.Provider', related_name='products', on_delete=models.DO_NOTHING, null=False)
    title = models.CharField(max_length=120, null=False)
    description = models.TextField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=19.99)

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
