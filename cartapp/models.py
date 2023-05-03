from django.db import models

# Create your models here.
class cartItem(models.Model):
    product_id = models.IntegerField(primary_key=True)
    price = models.FloatField(null=True)
    promotion_name = models.TextField(null=True)
    sales_country = models.TextField(null=True)
    added_to_cart = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self):
        return f'{self.product_id}, {self.price}, {self.promotion_name}, {self.sales_country},{self.quantity},'