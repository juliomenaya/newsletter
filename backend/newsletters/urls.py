from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NewslettersModelViewSet


router = DefaultRouter()
router.register(r'newsletters', NewslettersModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
