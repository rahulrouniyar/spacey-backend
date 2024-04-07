from django.contrib import admin
from .models import Customers, Product, Bill

# Register your models here.
admin.site.register(Customers)
admin.site.register(Product)
admin.site.register(Bill)
