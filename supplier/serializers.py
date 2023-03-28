from rest_framework import serializers
from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
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
            'sales_contact',
            'phone_number',
            'email',
            'created',
            'updated'
        ]
        read_only_fields = ('created', 'updated')
