from rest_framework import mixins, viewsets

from bundles.models import BundleRoom
from bundles.serializers import BundleRoomSerializer
from utils.pagination import BasePagination


class BundleViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pagination_class = BasePagination
    queryset = BundleRoom.objects.all().order_by("name")
    serializer_class = BundleRoomSerializer
