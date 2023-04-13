
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

    path('activity/', include("activity.urls")),
    path('category/', include("category.urls")),
    path('client/', include("client.urls")),
    path('equipment/', include("equipment.urls")),
    path('equipment_mantenance/', include("equipment_mantenance.urls")),
    path('laboratory/', include("laboratory.urls")),
    path('responsible_person/', include("responsible_person.urls")),
    path('supplier/', include("supplier.urls")),
]
