from rest_framework import viewsets
from rest_framework.response import Response

# from drf_spectacular.utils import extend_schema

from product.models import Category, Brand, Product
from product.serializers import CategorySerializer, BrandSerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing all categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # @extend_schema(responses=CategorySerializer)
    def list(self, request, *args, **kwargs):
        """
        Overriding list method to get only parent categories
        """
        categories = Category.objects.filter(parent__isnull=True)
        serializer = CategorySerializer(categories, many=True, context={"request": request})
        return Response(serializer.data)


class BrandViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing all brands.
    """

    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing all brands.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
