from rest_framework import serializers

from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'name', 'slug'
        ]
        read_only_fields = ['slug']
        lookup_fields = ['slug']
        extra_kwargs = {
            'url': {'lookup_fields': 'slug'}
        }


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'title', 'author', 'description', 'image', 'slug'
        ]
        read_only_fields = ['slug']
        lookup_fields = 'slug'
        extra_kwargs = {
            'url': {'lookup_fields': 'slug'}
        }
