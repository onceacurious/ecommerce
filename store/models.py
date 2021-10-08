from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):

    class CategoryManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset()

    name = models.CharField(max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    objects = models.Manager()
    categories = CategoryManager()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        elif self.slug != self.name:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    class ProductManager(models.Manager):

        def get_queryset(self):
            return super().get_queryset().filter(is_active=True)

    category = models.ForeignKey(
        Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='product_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        elif self.slug != self.title:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
