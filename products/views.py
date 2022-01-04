from typing import List
from django.db.models import Q
from django.http import Http404, response

from rest_framework import serializers

# from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Products,Category
from .serializers import ProductsSerializer,CategorySerializer

# Create your views here.
class CategoriesList(ListAPIView):
    """
    View to list all categories in the system
    """
    def get_queryset(self):
        categories = Category.objects.all()
        queryset = self.queryset
        queryset = categories

        return queryset

    def get(self,request,format=None):
        serializer = CategorySerializer(self.get_queryset(),many=True)
        return Response(serializer.data)

class ProductsList(ListAPIView):
    """
    View to list the first 10 products in the system arranged in an alphabetic order.
    """
    def get_queryset(self):
        products = Products.objects.all()[0:10]
        queryset = self.queryset
        queryset = products

        return queryset

    def get(self,request,format=None):
        serializer = ProductsSerializer(self.get_queryset(),many=True)
        return Response(serializer.data)

    class CategoryProducts(ListAPIView):
        """
        View to list all products in specific category
        """
        def get_queryset(self,category_slug):
            try:
                queryset = self.queryset
                queryset = Products.objects.filter(category__slug=category_slug) 
                return queryset
            except Products.DoesNotExist:
                raise Http404

        def get(self,request,category_slug,format=None):
            products = self.get_queryset(category_slug)
            serializer = ProductsSerializer(products,many=True)
            return Response(serializer.data)