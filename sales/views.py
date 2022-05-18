from xmlrpc.client import INTERNAL_ERROR
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.db.models import Q
from django.db import InternalError

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
    View to list sale items/receipts to store record of previous and old sales.
    """
    def get(self,request,format=None):
        receipts = ProductSales.objects.all()
        serializer = ProductSalesSerializer(receipts,many=True)
        return Response(serializer.data)


class ProductSalesDetailView(APIView):
    """
    View to get receipt information corresponding to a certain sale
    """
    def get_receipt(self,id,format=None):
        try:
            return ProductSales.objects.filter(sales_id=id)
        
        except ProductSales.DoesNotExist:
            raise Http404('Not found')

    def get(self,request,id,format=None):
        receipts = self.get_receipt(id)
        serializer = ProductSalesSerializer(receipts,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ProductSalesSerializer(data=request.data) #need to call is data valid first before passing data to serializer
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        return Response(serializer.errors)



# view to view an individual sale item
class SaleDetailView(APIView):
    """
    View to get an individual sale corresponding to given sales id and create
    a new sale
    """
    def get_sale(self,id,format=None):
        try: 
            return Sales.objects.get(id = id)
        except Sales.DoesNotExist:
            raise Http404('Not found')

    def get(self,request,id,format=None):
        sale = self.get_sale(id)
        serializer = SalesSerializer(sale)
        return Response(serializer.data)



        return Response(serializer.data)

# need a view to create a single sale which will be passed down on to saledetailview post
class CreateSaleView(APIView):
    """
    View to create a new sale
    """
    def create_sale(self,status,format=None):
        try:
            sale_status = SalesStatus.objects.get(status_name__exact=status)
            sale = Sales.objects.create(sales_status=sale_status)
            sale.save()
            return sale
        except:
            raise InternalError

    def post(self,request,format=None,*args,**kwargs): #learn about args and kwargs to change all these views to standards
        data = request.data
        sale = self.create_sale(data["status"])
        serializer = SalesSerializer(sale)

        return Response(serializer.data)
