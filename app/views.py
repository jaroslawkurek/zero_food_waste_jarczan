import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import ProductForm
from .models import Account, CustomAccountManager, Product
from .serializers import AccountSerializer, TokenSerializer
from .tokens import create_token


class AccountList(APIView):
    """
    List all accounts, or create a new account.
    """

    def post(self, request, format=None):
        serializer = AccountSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = Account.objects.get(email=serializer.data["email"])
        token = create_token(user)
        print(token)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ActivateUser(APIView):
    """
    Activate User
    """

    def post(self, request, format=None):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = Account.objects.get(id=serializer.data["id"])
        CustomAccountManager.activate_user(user)
        return Response(status=status.HTTP_200_OK)


def index(request):
    params = {"products": Product.objects.all()}
    return render(request, "app/product_list.html", params)


def register(request):
    return HttpResponse("register")


def login(request):
    return HttpResponse("login")


def logout(request):
    return HttpResponse("logout")


def user_view(request, user_id):
    return HttpResponse("user_view %s" % user_id)


def user_edit(request, user_id):
    return HttpResponse("user_edit %s" % user_id)


def user_remove(request, user_id):
    return HttpResponse("user_remove %s" % user_id)


def count_long_until_exp():
    today = datetime.datetime.now().date()
    all_products = Product.objects.all()
    count = 0
    for product in all_products:
        minus = product.exp_date - today
        if minus.days >= 30:
            count += 1
    return count


def count_close_to_exp():
    today = datetime.datetime.now().date()
    all_products = Product.objects.all()
    count = 0
    for product in all_products:
        minus = product.exp_date - today
        if minus.days <= 7 and minus.days >= 3:
            count += 1
    return count


def count_almost_expired():
    today = datetime.datetime.now().date()
    all_products = Product.objects.all()
    count = 0
    for product in all_products:
        minus = product.exp_date - today
        if minus.days <= 3 and minus.days >= 0:
            count += 1
    return count


def count_expired():
    today = datetime.datetime.now().date()
    all_products = Product.objects.all()
    count = 0
    for product in all_products:
        minus = product.exp_date - today
        if minus.days <= 0:
            count += 1
    return count


def product_list(request):
    products = Product.objects.all()
    all_products = products.count()
    long_until = count_long_until_exp()
    close_to_exp = count_close_to_exp()
    almost_expired = count_almost_expired()
    expired = count_expired()
    context = {
        "products": products,
        "all_products": all_products,
        "long_until": long_until,
        "close_to_exp": close_to_exp,
        "almost_expired": almost_expired,
        "expired": expired,
    }
    return render(request, "app/product_list.html", context)


def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/product_list/")
    context = {"form": form}
    return render(request, "app/add.html", context)


def update_product(request, pk):
    product = Product.objects.get(id=pk)
    # import pdb; pdb.set_trace()
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("/product_list/")
    context = {"form": form, "product": product}
    return render(request, "app/update.html", context)


def remove_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect("/product_list/")
    context = {"product": product}
    return render(request, "app/remove.html", context)
