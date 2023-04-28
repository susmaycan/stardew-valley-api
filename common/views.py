from rest_framework import mixins, viewsets

from common.models import Season
from common.serializers import SeasonSerializer


class SeasonViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Season.objects.all().order_by("id")
    serializer_class = SeasonSerializer
