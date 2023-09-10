from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet

product_router = DefaultRouter()
product_router.register("category", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(product_router.urls), name="product"),
]
