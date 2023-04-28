from django.test import TestCase
from rest_framework.status import HTTP_200_OK

from common.tests.factories import SeasonFactory
from utils.test_utils import PATH, make_api_call


class SeasonTestCase(TestCase):
    def setUp(self):
        SeasonFactory(name="Primavera")
        self.summer = SeasonFactory(name="Verano")
        self.autumn = SeasonFactory(name="Otoño")
        self.winter = SeasonFactory(name="Invierno")

    def test_retrieve_season_list_ok(self):
        response = make_api_call(route=PATH.SEASONS, query_params={})

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertIsNotNone(response.content)
        self.assertEqual(len(response.content), 4)
