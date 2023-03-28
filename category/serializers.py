from rest_framework import serializers
from .models import Category, SubCategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'created',
            'updated'
        ]
        read_only_fields = ('created', 'updated')


class SubCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source='category.name', read_only=True)

    class Meta:
        model = SubCategory
        fields = [
            'id',
            'category',
            'category_name',
            'name',
            'created',
            'updated'
        ]
        read_only_fields = ('created', 'updated')
