from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120, null=False)
    description = models.TextField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=19.99)

    def __str__(self):
        return self.title

    de
