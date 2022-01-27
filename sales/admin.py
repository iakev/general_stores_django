from django.contrib import admin

from .models import Sales,ProductSales, SalesStatus
# Register your models here.

admin.site.register(SalesStatus)
admin.site.register(ProductSales)
admin.site.register(Sales)
