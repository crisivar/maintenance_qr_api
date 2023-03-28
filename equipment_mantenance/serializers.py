from rest_framework import serializers

from activity.models import Activity
from category.models import SubCategory
from .models import EquipmentMaintenance


class EquipmentMaintenanceSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Activity.objects.all())
    subcategory = serializers.PrimaryKeyRelatedField(
        queryset=SubCategory.objects.all())

    class Meta:
        model = EquipmentMaintenance
        fields = [
            'activity',
            'image',
            'subcategory',
            'observations',
            'pending',
            'created',
            'updated',
        ]
        read_only_fields = ('created', 'updated')
