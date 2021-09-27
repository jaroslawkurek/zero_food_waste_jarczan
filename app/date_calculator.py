from datetime import date
from .models import Product

today = date.today()
all_products = Product.objects.get.all()


def print_today():
    return str(today)


def count_long_until():
    count = 0
    for product in all_products:
        while product.exp_date - today >= 30:
            count += 1
    return count

print(count_long_until)
