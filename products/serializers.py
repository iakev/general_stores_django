"""
 Serializers get information from the database and turn it into JSON for renderig in front-end in this project Vue
"""
from rest_framework import serializers

from .models import Products,Category

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = (
            'name',
            'category',
            'code',
            'slug',
            'pack_type',
            'quantity',
            'description',
            'rate_in',
            'rate_out_retail',
            'rate_out_wholesale',
            'date_added',
            'get_absolute_url'
        )
 
class CategorySerializer(serializers.ModelSerializer):

    products = ProductsSerializer(many=True)

    class Meta:
        model = Category
        fields =(
            'id',
            'name',
            'products',
            'get_absolute_url',
            'get_thumbnail',
        )