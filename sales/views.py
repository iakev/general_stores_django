from django.db.models.query import QuerySet
from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.db.models import Q

from rest_framework import status,authentication,permissions,viewsets
from rest_framework import generics
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from .models import Sales,ProductSales,SalesStatus
from .serializers import SalesSerializer,ProductSalesSerializer


class SalesList(APIView):
    """
    View to list all sales in the system or create sales from the front-end form data.
    """
    def get(self,request,format=None):
        sales = Sales.objects.all()
        serializer = SalesSerializer(sales,many=True)
        return Response(serializer.data)



class ProductsSalesList(APIView):
    """
    class to list sale items/receipts to store record of previous and old sales.
    """
    def get(self,request,format=None):
        receipts = ProductSales.objects.all()
        serializer = ProductSalesSerializer(receipts,many=True)
        return Response(serializer.data)


    def post(self,request,format=None):
        serializer = ProductSalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() # current problem leads to serializers.py line number 33
            return Response(serializer.data)
        return Response(serializer.errors)