from rest_framework import serializers

from products.serializers import ProductsSerializer
from .models import Sales,ProductSales,SalesStatus

class ProductSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSales
        fields = (
            'id',
            'products',
            'sales',            
            'quantity_sold',
            'price_per_unit_retail',
            'price_per_unit_wholesale',
            'price',
            'is_retail',
        )
 

    def create(self,validated_data):
        """
        Create and return new ProductSales instance/object, given validated data
        """
        status = SalesStatus.objects.create()
        sale = Sales.objects.create(sales_status=status,sale_amount=0.00)
        validated_data["sales"] = sale
        instance = ProductSales.objects.create(**validated_data)
        return instance


class SalesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Sales
        fields = (
            'id',
            'products',
            'sale_amount',
            'sale_amount_paid',            
            'time_created',
            'time_paid',
            'sales_status',
        )
        
   



