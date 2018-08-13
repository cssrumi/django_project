import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

import django

django.setup()

import random
from products.models import Provider, Product
from faker import Faker
from decimal import Decimal

fake_gen = Faker()
coffee_types = ['Coffee Arabica', 'Coffee Robusta', 'Coffea Arabica', 'Coffea Robusta']


def add_coffee_types():
    t = random.choice(coffee_types)
    return t


def populate(n=5):
    for entry in range(n):
        # PROVIDER
        fake_name = fake_gen.company()
        fake_description = fake_gen.paragraphs(
            nb=3,
            ext_word_list=None
        )
        fake_location = fake_gen.address()

        # Create the new Provider
        provider_record = Provider.objects.get_or_create(
            name=fake_name,
            description=fake_description,
            location=fake_location
        )[0]

        # PRODUCT
        for _ in range(random.randint(0, 5)):
            # PRODUCT
            product_title = add_coffee_types()
            fake_prod_description = fake_gen.paragraphs(nb=3, ext_word_list=None)
            fake_price = Decimal(random.randrange(10, 1000) + 0.99)
            fake_price = round(fake_price, 2)
            product_record = Product.objects.get_or_create(
                provider=provider_record,
                title=product_title,
                description=fake_prod_description,
                price=fake_price
            )[0]


if __name__ == '__main__':
    print('populating script!')
    populate()
    print('populating complete!')
