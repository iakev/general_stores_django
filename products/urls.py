from django.urls import path, include

from products import views

urlpatterns = [
    path('categories/',views.CategoriesList().as_view()),
    path('products/',views.ProductsList.as_view()),
    # path('products/<slug:category_slug>/',views.Ca)
]