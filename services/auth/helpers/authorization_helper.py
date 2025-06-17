import requests

from services.general.helpers.base_helper import BaseHelper


class AuthorizationHelper(BaseHelper):
    ENDPOINT_PREFIX = "/auth"

    REGISTER_ENDPOINT = f"{ENDPOINT_PREFIX}/register/"
    LOGIN_ENDPOINT = f"{ENDPOINT_PREFIX}/login/"

    def post_register(self, data: dict) -> requests.Response:
        resp = self.api_utils.post(self.REGISTER_ENDPOINT, data=data)
        return resp

    def post_login(self, data: dict) -> requests.Response:
        resp = self.api_utils.post(self.LOGIN_ENDPOINT, data=data)
        return resp
