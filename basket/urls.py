from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'basket'

router = DefaultRouter()
router.register(r'', BasketViewSet, basename='basket_summary')

urlpatterns = router.urls
