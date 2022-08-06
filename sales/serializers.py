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
        #retrieve sale object using sale primary key and adding it to validated data dictionary
        
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
        # depth = 1
   
    def update(self, instance, validated_data):
        # product_ids = validated_data.pop('products')
        print (validated_data)
        products = instance.products
        print(products)
        # instance.products = validated_data.get('products',instance.products)
        instance.save()
        return instance



