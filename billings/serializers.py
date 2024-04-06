from rest_framework.serializers import ModelSerializer
from .models import Customers, Product, Category


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CartSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
