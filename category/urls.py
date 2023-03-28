from django.urls import path
from .views import (
    CategoryList,
    CategoryDetail,
    SubCategoryList,
    SubCategoryDetail
)

urlpatterns = [
    path('', CategoryList.as_view(), name='category-list'),
    path('<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('subcategory', SubCategoryList.as_view(), name='subcategory-list'),
    path('subcategory/<int:pk>/', SubCategoryDetail.as_view(),
         name='subcategory-detail')
]
