from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet

app_name = 'store'

router = DefaultRouter()
router.register(r'book', CategoryViewSet, basename='category_list')
router.register(r'', ProductViewSet, basename='product_detail')

urlpatterns = router.urls
