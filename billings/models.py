from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Employees(AbstractUser):
    pass


class Customers(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.PositiveBigIntegerField()


# class Category(models.Model):
#     title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # category = models.ForeignKey(
    #         Category, on_delete=models.CASCADE, related_name="category"
    #     )
    description = models.TextField(max_length=1000)


class Bill(models.Model):
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


# class Order(models.Model):
#     customer = models.ForeignKey(
#         Customers, on_delete=models.CASCADE, related_name="customers"
#     )
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateField(auto_now=True)


# class Cart(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_id")
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name="product_id"
#     )
#     quantity = models.PositiveIntegerField()

#     class Meta:
#         unique_together = ("order", "product")
