from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    class CategoryManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    objects = models.Manager()
    categories = CategoryManager()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    class ProductManager(models.Manager):

        def get_queryset(self):
            return super().get_queryset().filter(is_active=True)

    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='image/', default='image/default_house.png')
    slug = models.SlugField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    products = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
        # Decending order: last added will be on the top
        ordering = ('-created',)

    def __str__(self):
        return self.title
