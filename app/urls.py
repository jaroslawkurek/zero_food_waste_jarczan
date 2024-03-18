from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("user_view/<int:user_id>/", views.user_view, name="user_view"),
    path("user_edit/<int:user_id>/", views.user_edit, name="user_edit"),
    path("user_remove/<int:user_id>/", views.user_remove, name="user_remove"),
    path("product_list/", views.product_list, name="product_list"),
    path("add_product/", views.add_product, name="add_product"),
    path("update_product/<str:pk>/", views.update_product, name="update_product"),
    path("remove_product/<str:pk>/", views.remove_product, name="remove_product"),
]
