from rest_framework import serializers
from client.models import Client
from laboratory.models import Laboratory
from responsible_person.models import ResponsiblePerson
from .models import Equipment


class EquipmentSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    laboratory = serializers.PrimaryKeyRelatedField(
        queryset=Laboratory.objects.all())
    responsible_person = serializers.PrimaryKeyRelatedField(
        queryset=ResponsiblePerson.objects.all())

    class Meta:
        model = Equipment
        fields = [
            'id',
            'image',
            'client',
            'laboratory',
            'responsible_person',
            'name', 'category',
            'subcategory', 'brand',
            'model',
            'serial_number',
            'billing_internal_code',
            'entry_price',
            'selling_price',
            'unit',
            'minimum_inventory',
            'is_active',
            'created',
            'updated'
        ]
        read_only_fields = ('created', 'updated')
