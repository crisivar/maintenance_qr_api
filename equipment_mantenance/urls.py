from django.urls import path
from .views import EquipmentMaintenanceList, EquipmentMaintenanceDetail

urlpatterns = [
    path('', EquipmentMaintenanceList.as_view(),
         name='equipment-maintenance-list'),
    path('<int:pk>/', EquipmentMaintenanceDetail.as_view(),
         name='equipment-maintenance-detail'),
]
