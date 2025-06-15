import requests

from src.services.general.helpers.base_helper import BaseHelper


class TeacherHelper(BaseHelper):
    ENDPOINT_PREFIX = "/teachers"

    ROOT_ENDPOINT = f"{ENDPOINT_PREFIX}/"

    def post_teacher(self, json: dict) -> requests.Response:
        resp = self.base_api_client.post(self.ROOT_ENDPOINT, json=json)
        return resp

    def get_teacher_by_id(self, teacher_id: int) -> requests.Response:
        resp = self.base_api_client.get(f"{self.ROOT_ENDPOINT}{teacher_id}")
        return resp


    def delete_teacher_by_id(self, teacher_id: int) -> requests.Response:
        resp = self.base_api_client.delete(f"{self.ROOT_ENDPOINT}{teacher_id}")
        return resp