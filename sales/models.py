from django.db import models
from django.db.models import constraints
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.conf import settings

import decimal


# Create your models here.


class SalesStatus(models.Model):
    status_name = models.CharField(max_length=255)

    def __str__(self):
        return self.status_name

class Sales(models.Model):
    products = models.ManyToManyField("products.Products",through="ProductSales",related_name="product_in_sales")
    time_created = models.DateTimeField(auto_now_add=True)
    time_paid = models.DateTimeField(default=timezone.now,null=True)
    sale_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00,blank=True)
    sale_amount_paid = models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=0.00)    
    tax_amount = models.IntegerField(blank=True,default=0)
    sales_status = models.ForeignKey(SalesStatus,on_delete=models.CASCADE,related_name="status",blank=True,default="Sold")
    # user_has_role_id =models.ForeignKey(user=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Sales"

    def __str__(self):
        identifier = self.id
        return "Sale_" + str(identifier)

class ProductSales(models.Model):
    products = models.ForeignKey("products.Products",on_delete=models.CASCADE,related_name="link_to_products")
    sales = models.ForeignKey(Sales,on_delete=models.CASCADE,related_name="link_to_sales",blank=True)
    quantity_sold = models.IntegerField()
    price_per_unit_retail = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    price_per_unit_wholesale = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    price = models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=0.0) #product of price_per_unit(respectively if retail/wholesale) and quantity_sold 
    tax_amount = models.IntegerField(null=True,blank=True)
    is_retail = models.BooleanField(default=True)
    class Meta:
            constraints.UniqueConstraint(fields=['products','sales'], name="unique_selling")
        
    #Database working as expected using models however these methods should be placed in serializers since we
    #use API to create, update and delete from the front-end
    def save(self,*args,**kwargs):
        if self.price:
            pass
        else:
            if self.is_retail:
                self.price = self.price_per_unit_retail * self.quantity_sold
            else:
                self.price = self.price_per_unit_wholesale * self.quantity_sold
        
        #updating the total sales amount with individual prices 
        self.sales.save()
        # updating product quantity as per the quantity sold
        self.products.quantity -= self.quantity_sold
        self.products.save()

        super().save(*args,**kwargs)


    def __str__(self):
        return self.products.name + '_item_sale'