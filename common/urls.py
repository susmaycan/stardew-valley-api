from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from common.views import SeasonViewSet

router = routers.DefaultRouter()
router.register(r"seasons", SeasonViewSet, basename="seasons")


urlpatterns = [
    path("", include(router.urls)),
]
