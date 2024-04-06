from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse

# from .models import Customers, Category, Product, Order, Cart
# from .serializers import (
#     CustomerSerializer,
#     CategorySerializer,
#     ProductSerializer,
#     OrderSerializer,
#     CartSerializer,
# )


# Create your views here.
def index(request):
    return HttpResponse("Hello this is rahul rouniyar from home")


# class CustomerViewset(ModelViewSet):
#     model = Customers
#     serializer_class = CustomerSerializer


# class ProductViewset(ModelViewSet):
#     model = Product
#     serializer_class = ProductSerializer


# class CategoryViewset(ModelViewSet):
#     model = Category
#     serializer_class = CategorySerializer


# class OrderViewset(ModelViewSet):
#     model = Order
#     serializer_class = OrderSerializer


# class CartViewset(ModelViewSet):
#     model = Cart
#     serializer_class = CartSerializer
