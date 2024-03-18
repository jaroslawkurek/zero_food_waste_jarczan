from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions_on_top = True
    list_display = ("name", "quantity", "exp_date")
