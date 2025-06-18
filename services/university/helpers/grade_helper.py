import requests

from services.general.helpers.base_helper import BaseHelper


class GradeHelper(BaseHelper):
    ENDPOINT_PREFIX = "/grades"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_grade(self, data: dict) -> requests.Response:
        resp = self.api_utils.post(self.ROOT_ENDPOINT, data=data)
        return resp
