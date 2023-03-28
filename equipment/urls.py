from django.urls import path
from .views import EquipmentList, EquipmentDetail

urlpatterns = [
    path('', EquipmentList.as_view(), name='equipment-list'),
    path('<int:pk>/', EquipmentDetail.as_view(), name='equipment-detail'),
]
