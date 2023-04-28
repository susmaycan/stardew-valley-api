from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from bundles.views import BundleViewSet

router = routers.DefaultRouter()
router.register(r"bundles", BundleViewSet, basename="bundles")


urlpatterns = [
    path("", include(router.urls)),
]
