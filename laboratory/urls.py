from django.urls import path
from .views import LaboratoryList, LaboratoryDetail

urlpatterns = [
    path('', LaboratoryList.as_view(), name='laboratory-list'),
    path('<int:pk>/', LaboratoryDetail.as_view(), name='laboratory-detail'),
]
