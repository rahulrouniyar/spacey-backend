from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User, Group
from .models import Customers, Product, Bill


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class BillSerializer(ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"


# class CategorySerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"


# class OrderSerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"


# class CartSerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"
