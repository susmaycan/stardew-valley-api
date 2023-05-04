from rest_framework import serializers

from bundles.models import Bundle, BundleItem, BundleRoom, Reward


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields = (
            "name",
            "icon",
        )


class BundleRoomSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    bundles = serializers.SerializerMethodField()
    reward = RewardSerializer()

    class Meta:
        model = BundleRoom
        fields = ("id", "name", "reward", "bundles")

    def get_bundles(self, obj):
        request = self.context["request"]
        qs = Bundle.objects.filter(room__id=obj.id)
        serializer = BundleSerializer(
            qs, read_only=True, many=True, context={"request": request}
        )
        return serializer.data


class BundleItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    season = serializers.SlugRelatedField(read_only=True, slug_field="name", many=True)

    class Meta:
        model = BundleItem
        fields = (
            "id",
            "name",
            "image",
            "description",
            "season",
        )


class BundleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    items = serializers.SerializerMethodField()
    reward = RewardSerializer()

    class Meta:
        model = Bundle
        fields = ("id", "name", "image", "reward", "items", "completed_number")

    def get_items(self, obj):
        request = self.context["request"]
        season_param = request.query_params.get("season")
        name_param = request.query_params.get("name")
        qs = BundleItem.objects.filter(bundle__id=obj.id)
        if season_param:
            qs = qs.filter(season__id=season_param)
        if name_param:
            qs = qs.filter(name__icontains=name_param)

        serializer = BundleItemSerializer(qs, read_only=True, many=True)
        return serializer.data
