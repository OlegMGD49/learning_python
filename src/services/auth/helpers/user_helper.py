import requests

from src.services.general.helpers.base_helper import BaseHelper


class UserHelper(BaseHelper):
    ENDPOINT_PREFIX = "/users"

    ME_ENDPOINT = f"{ENDPOINT_PREFIX}/me/"


    def get_me(self)->requests.Response:
        resp = self.base_api_client.get(self.ME_ENDPOINT)
        return resp
