from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'id',
            'client',
            'laboratory',
            'responsible_person',
            'category',
            'subcategory',
            'equipment',
            'user',
            'date',
            'code',
            'created',
            'updated',
        ]
        read_only_fields = ('created', 'updated')
