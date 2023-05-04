from django.test import TestCase
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND

from bundles.tests.factories import (BundleFactory, BundleItemFactory,
                                     BundleRoomFactory)
from common.tests.factories import SeasonFactory
from utils.test_utils import PATH, make_api_call


class SeasonTestCase(TestCase):
    def setUp(self):
        self.spring = SeasonFactory(name="Primavera")
        self.summer = SeasonFactory(name="Verano")
        self.autumn = SeasonFactory(name="Otoño")
        self.winter = SeasonFactory(name="Invierno")

        bundle_room = BundleRoomFactory(name="Lote artesanal")
        bundle = BundleFactory(room=bundle_room, name="Origen animal")
        bundle_item1 = BundleItemFactory(bundle=bundle, name="Huevos")
        bundle_item2 = BundleItemFactory(bundle=bundle, name="Huevos XXL")
        bundle_item3 = BundleItemFactory(bundle=bundle, name="Leche")
        bundle_item1.season.set([self.spring])
        bundle_item2.season.set([self.winter])
        bundle_item3.season.set([self.summer, self.autumn])

        self.artisanal_bundle = bundle_room
        self.animal_sub_bundle = bundle

        bundle_room2 = BundleRoomFactory(name="Pecera")
        bundle3 = BundleFactory(room=bundle_room2)
        bundle_item4 = BundleItemFactory(bundle=bundle3, name="Pez sol")
        bundle_item4.season.set([self.autumn])

        self.fish_bundle = bundle_room

    def make_retrieve_bundle_list_call(self, query_params={}):
        url = PATH.BUNDLES
        return make_api_call(route=url, query_params=query_params)

    def make_retrieve_bundle_call(self, uuid):
        return make_api_call(route=PATH.BUNDLES + "%s/" % (uuid))

    def test_retrieve_bundle_list_ok(self):
        response = self.make_retrieve_bundle_list_call()

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 2)

    def test_retrieve_animal_list_filter_name(self):

        query_param = {"name": "huevos"}
        response = self.make_retrieve_bundle_list_call(query_params=query_param)

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 2)
        artisanal_bundle_response = response.content["results"][0]
        self.assertEqual(len(artisanal_bundle_response["bundles"][0]["items"]), 2)
        fish_bundle_response = response.content["results"][1]
        self.assertEqual(len(fish_bundle_response["bundles"][0]["items"]), 0)

    def test_retrieve_animal_list_filter_season(self):

        query_param = {"season": self.autumn.id}
        response = self.make_retrieve_bundle_list_call(query_params=query_param)

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.content["count"], 2)
        artisanal_bundle_response = response.content["results"][0]
        self.assertEqual(len(artisanal_bundle_response["bundles"][0]["items"]), 1)
        fish_bundle_response = response.content["results"][1]
        self.assertEqual(len(fish_bundle_response["bundles"][0]["items"]), 1)

    def test_retrieve_animal_by_id_ok(self):
        response = self.make_retrieve_bundle_call(uuid=self.artisanal_bundle.id)

        self.assertEqual(response.status_code, HTTP_200_OK)
        content = response.content
        self.assertEqual(content["name"], self.artisanal_bundle.name)
        self.assertEqual(content["reward"]["name"], self.artisanal_bundle.reward.name)
        self.assertEqual(len(content["bundles"]), 1)
        animal_sub_bundle = content["bundles"][0]
        self.assertEqual(animal_sub_bundle["name"], self.animal_sub_bundle.name)
        self.assertEqual(
            animal_sub_bundle["reward"]["name"], self.animal_sub_bundle.reward.name
        )
        self.assertEqual(len(animal_sub_bundle["items"]), 3)

    def test_retrieve_bundle_by_id_not_found(self):
        response = self.make_retrieve_bundle_call(uuid=435345345)
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)
