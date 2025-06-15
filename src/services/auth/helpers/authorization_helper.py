import requests

from src.services.general.helpers.base_helper import BaseHelper


class AuthorizationHelper(BaseHelper):
    ENDPOINT_PREFIX = "/auth"

    REGISTER_ENDPOINT = f"{ENDPOINT_PREFIX}/register/"
    LOGIN_ENDPOINT = f"{ENDPOINT_PREFIX}/login/"

    def post_register(self, data: dict) -> requests.Response:
        resp = self.base_api_client.post(self.REGISTER_ENDPOINT, data=data)
        return resp

    def post_login(self, data: dict) -> requests.Response:
        resp = self.base_api_client.post(self.LOGIN_ENDPOINT, data=data)
        return resp
