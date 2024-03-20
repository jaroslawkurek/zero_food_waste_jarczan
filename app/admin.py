from django.contrib import admin

from .models import Account, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions_on_top = True
    list_display = ("name", "quantity", "exp_date")


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    actions_on_top = True
    list_display = ("email", "display_name")
