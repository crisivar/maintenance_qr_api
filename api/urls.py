
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('activity/', include("activity.urls")),
    path('category/', include("category.urls")),
    path('client/', include("client.urls")),
    path('equipment/', include("equipment.urls")),
    path('equipment_mantenance/', include("equipment_mantenance.urls")),
    path('laboratory/', include("laboratory.urls")),
    path('responsible_person/', include("responsible_person.urls")),
    path('supplier/', include("supplier.urls")),
]
