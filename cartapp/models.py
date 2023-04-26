from django.db import models

# Create your models here.
class cartItem(models.Model):
    product_id = models.IntegerField(primary_key=True)
    price = models.FloatField()
    promotion_name = models.TextField()
    sales_country = models.TextField()
    added_to_cart = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product_id}, {self.price}, {self.promotion_name}, {self.sales_country},'