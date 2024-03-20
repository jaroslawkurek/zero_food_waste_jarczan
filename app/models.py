from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.contrib.auth.password_validation import validate_password
from django.db import models


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, password, display_name=""):
        validate_password(password)
        user = self.model(email=self.normalize_email(email), display_name=display_name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save()
        return user

    def activate_user(user):
        user.is_active = True
        user.save()


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True)
    display_name = models.CharField(max_length=60, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = CustomAccountManager()

    def __str__(self):
        return self.email


class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    exp_date = models.DateField("expiration date")

    def __str__(self):
        return self.name
