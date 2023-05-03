from django.conf import settings
from django.db import models
from django.utils import timezone

import shopping_table.models


# Create your models here.

class maintable(models.Model):

    product_id = models.IntegerField(primary_key=True)
    price = models.FloatField()
    promotion_name = models.TextField()
    sales_country = models.TextField()

    def __str__(self):
        return f'{self.product_id}, {self.price}, {self.promotion_name}, {self.sales_country},'

class detailtable(models.Model):
    product_id = models.IntegerField(null=True)
    promotion_name = models.TextField(null=True)
    sales_country = models.TextField(null=True)
    sales_volume = models.IntegerField(null=True)
    negative_comment = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    invoice_date = models.TextField(null=True)
    supplier = models.TextField(null=True)
    brand_name = models.TextField(null=True)

    def __str__(self):
        return f'{self.product_id}, {self.price}, {self.promotion_name}, {self.sales_country}, {self.sales_volume}, {self.negative_comment}, {self.invoice_date}, {self.supplier}, {self.brand_name},'

