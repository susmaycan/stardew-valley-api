from rest_framework import serializers

from common.models import Season


class SeasonSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Season
        fields = ("id", "name")
