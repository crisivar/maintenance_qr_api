from django.urls import path
from .views import SupplierList, SupplierDetail

urlpatterns = [
    path('', SupplierList.as_view(), name='supplier-list'),
    path('<int:pk>/', SupplierDetail.as_view(), name='supplier-detail'),
]
