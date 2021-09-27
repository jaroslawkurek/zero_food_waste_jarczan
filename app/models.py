from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    exp_date = models.DateField('expiration date')

    def __str__(self):
        return self.name
