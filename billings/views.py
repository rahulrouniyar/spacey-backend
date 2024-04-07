from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication

from django.http import HttpResponse
from .models import Customers, Product, Bill
from .serializers import CustomerSerializer, ProductSerializer, BillSerializer


# Create your views here.
def index(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home Page</title>
    </head>
    <body>
        <h1>Admin username and password:</h1>
        <u>
            <li>Username: admin</li>
            <li>Password: testpass</li>
            <li>Token: </li>
        <h1>URLs are as follows:</h1>
        <ul>
            <li>/api/customers</li>
            <li>/api/products</li>
            <li>/api/bills</li>
            <li>/api/schema/swagger-ui</li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html_content)


class CustomerViewset(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]


class BillViewSet(ModelViewSet):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

    def perform_create(self, serializer):
        total_amount = sum(
            product.price for product in serializer.validated_data["products"]
        )
        serializer.save(total_amount=total_amount)


# class CategoryViewset(ModelViewSet):
#     model = Category
#     serializer_class = CategorySerializer


# class OrderViewset(ModelViewSet):
#     model = Order
#     serializer_class = OrderSerializer


# class CartViewset(ModelViewSet):
#     model = Cart
#     serializer_class = CartSerializer
