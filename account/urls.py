from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import UserViewSet


app_name = 'account'

router = DefaultRouter()
router.register('account', UserViewSet, basename='account_auth')

urlpatterns = router.urls
