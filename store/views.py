from django.shortcuts import get_object_or_404, render
from rest_framework.viewsets import ModelViewSet

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.categories.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductViewSet(ModelViewSet):
    queryset = Product.products.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
