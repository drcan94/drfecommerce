from rest_framework import viewsets, status
from rest_framework.response import Response
from product.models import Category, Brand, Product
from product.serializers import CategorySerializer, BrandSerializer, ProductSerializer
from django.shortcuts import get_object_or_404


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing all categories.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        """
        Overriding list method to get only parent categories
        """
        categories = Category.objects.filter(parent__isnull=True)
        serializer = CategorySerializer(categories, many=True, context={"request": request})
        return Response(serializer.data)

    # def list(self, request):
    #     queryset = Category.objects.all()
    #     serializer = CategorySerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Category.objects.all()
    #     category = get_object_or_404(queryset, pk=pk)
    #     serializer = CategorySerializer(category)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = CategorySerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     category = Category.objects.get(pk=pk)
    #     serializer = CategorySerializer(category, data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def partial_update(self, request, pk=None):
    #     category = Category.objects.get(pk=pk)
    #     serializer = CategorySerializer(category, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def destroy(self, request, pk=None):
    #     category = Category.objects.get(pk=pk)
    #     category.delete()
    #     return Response({"message": "Category deleted successfully!"})
