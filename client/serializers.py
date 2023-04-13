from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = [
            'id',
            'business_name',
            'nit',
            'tax_responsibility',
            'taxpayer_type',
            'responsibility_type',
            'country',
            'department',
            'city',
            'postal_code',
            'billing_email',
            'purchasing_contact',
            'phone_number',
            'email',
            'created',
            'updated'
        ]
        read_only_fields = ('created', 'updated')
