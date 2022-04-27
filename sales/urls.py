from django.urls import path
from django.urls.resolvers import URLPattern

from sales import views

urlpatterns = [
    path('sales/',views.SalesList.as_view()),
    path('sales/receipts/',views.ProductsSalesList.as_view()),
    path('sales/<id>',views.SaleDetailView.as_view())
]