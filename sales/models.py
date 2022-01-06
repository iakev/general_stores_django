from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.conf import settings


# Create your models here.


class SalesStatus(models.Model):
    status_name = models.CharField(max_length=255)


class Sales(models.Model):
    products = models.ManyToManyField("products.Products",through="ProductSales",related_name="products_sales")
    time_created = models.DateTimeField(auto_now_add=True)
    time_paid = models.DateTimeField(default=timezone.now,null=True)
    tax_amount = models.IntegerField(null=True)
    sales_status = models.ForeignKey(SalesStatus,on_delete=models.CASCADE,related_name="status")
    # user_has_role_id =models.ForeignKey(user=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sales"

class ProductSales(models.Model):
    quantity_sold = models.IntegerField()
    price_per_unit_retail = models.IntegerField()
    price_per_unit_wholesale = models.IntegerField()
    price = models.IntegerField() #product of price_per_unit(respectively if retail/wholesale) and quantity_sold 
    tax_amount = models.IntegerField(null=True)
    sales = models.ForeignKey(Sales,on_delete=models.CASCADE,related_name="sales")
    products = models.ForeignKey("products.Products",on_delete=models.CASCADE,related_name="products")
    is_retail = models.BooleanField()

    def save(self,*args,**kwargs):
        if self.is_retail:
            self.price = self.price_per_unit_retail * self.quantity_sold

        else:
            self.price = self.price_per_unit_wholesale * self.quantity_sold

        super().save(*args,**kwargs)