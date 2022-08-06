from django.urls import path, include

from products import views

urlpatterns = [
    path('categories/',views.CategoriesList().as_view()),
    path('products/',views.ProductsList.as_view()),
    path('categories/<slug:category_slug>/',views.CategoryProducts.as_view()),
    path('products/search/',views.search),
    path('products/sales_search/',views.sale_product_search),
    path('products/<id>/',views.ProductRetrieval.as_view())
]