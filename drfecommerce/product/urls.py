from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product.views import CategoryViewSet, BrandViewSet, ProductViewSet

product_router = DefaultRouter()
product_router.register(
    "category",
    CategoryViewSet,
    basename="category",
)
product_router.register(
    "brand",
    BrandViewSet,
    basename="brand",
)
product_router.register(
    "product",
    ProductViewSet,
    basename="product",
)


urlpatterns = [
    path("", include(product_router.urls), name="product"),
]
