from django.contrib import admin
from .models import Employees, Customers, Category, Product

# Register your models here.
admin.site.register(Employees)
admin.site.register(Customers)
admin.site.register(Category)
admin.site.register(Product)
