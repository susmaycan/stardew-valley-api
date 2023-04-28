import json

from rest_framework.test import APIClient


class PATH:
    BUNDLES = "/bundles/"
    SEASONS = "/seasons/"


class CustomResponse:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content


def make_api_call(route, query_params={}):
    client = APIClient()

    if query_params:
        route = route.__add__("?")
        for key, value in query_params.items():
            route = f"{route}{key}={value}&"

    response = client.get(route)

    content = None
    if response.content:
        json_response = json.loads(response.content)
        content = json_response

    return CustomResponse(status_code=response.status_code, content=content)
