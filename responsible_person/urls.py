from django.urls import path
from .views import ResponsiblePersonList, ResponsiblePersonDetail

urlpatterns = [
    path('', ResponsiblePersonList.as_view(), name='responsiblepersons-list'),
    path('<int:pk>/', ResponsiblePersonDetail.as_view(),
         name='responsiblepersons-detail'),
]
