from rest_framework import serializers
from client.models import Client
from .models import ResponsiblePerson


class ResponsiblePersonSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all())

    class Meta:
        model = ResponsiblePerson
        fields = [
            'name',
            'phone',
            'email',
            'client',
            'created',
            'updated'
        ]
        read_only_fields = ('created', 'updated')
