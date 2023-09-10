# category serializer
from rest_framework import serializers
from product.models import Category, Brand, Product


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField(source="pk")
    parent_id = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)

        # fields listesinden "children" alanını kaldır
        self.fields.pop("children", None)

        # "children" alanını en sona eklemek için
        self.fields["children"] = serializers.SerializerMethodField()

    def get_parent_id(self, obj):
        if obj.parent:
            return obj.parent.pk
        return None

    def get_children(self, obj):
        children = Category.objects.filter(parent=obj.pk)
        serializer = CategorySerializer(children, many=True, context=self.context)
        return serializer.data


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
