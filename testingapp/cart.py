import requests
from . import models

# cart fuctions

def add_to_cart(product):

    check = models.cart.objects.create(
        Name = product.Name,
        description = product.description 
    )

    check.save()
    check.refresh_from_db

    




