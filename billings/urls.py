from django.urls import path, include
from .views import CustomerViewset, ProductViewset, BillViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r"customers", CustomerViewset)
router.register(r"products", ProductViewset)
router.register(r"bills", BillViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
