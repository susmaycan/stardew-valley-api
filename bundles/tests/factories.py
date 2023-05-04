from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from bundles.models import Bundle, BundleItem, BundleRoom, Reward


class RewardFactory(DjangoModelFactory):
    name = Faker("pystr", min_chars=1, max_chars=50)
    icon = Faker("pystr", min_chars=1, max_chars=50)

    class Meta:
        model = Reward


class BundleRoomFactory(DjangoModelFactory):
    name = Faker("pystr", min_chars=1, max_chars=50)
    reward = SubFactory(RewardFactory)

    class Meta:
        model = BundleRoom


class BundleFactory(DjangoModelFactory):
    name = Faker("pystr", min_chars=1, max_chars=50)
    reward = SubFactory(RewardFactory)
    room = SubFactory(BundleRoomFactory)
    image = Faker("pystr", min_chars=1, max_chars=200)
    icon = Faker("pystr", min_chars=1, max_chars=200)

    class Meta:
        model = Bundle


class BundleItemFactory(DjangoModelFactory):
    name = Faker("pystr", min_chars=1, max_chars=50)
    description = Faker("pystr", min_chars=1, max_chars=50)
    image = Faker("pystr", min_chars=1, max_chars=200)

    bundle = SubFactory(BundleFactory)

    class Meta:
        model = BundleItem
