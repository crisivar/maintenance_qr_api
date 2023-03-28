from rest_framework import serializers
from .models import Laboratory


class LaboratorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Laboratory
        fields = [
            'laboratory_name'
            'responsible_person'
            'position'
            'phone'
            'email'
            'username'
            'password'
            'active'
            'created'
            'updated'
        ]
        read_only_fields = ('created', 'updated')
