from factory import Faker
from factory.django import DjangoModelFactory

from common.models import Season


class SeasonFactory(DjangoModelFactory):
    name = Faker("pystr", min_chars=1, max_chars=50)

    class Meta:
        model = Season
