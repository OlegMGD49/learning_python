import json

import curlify
import requests
from requests import Session

from logger.logger import Logger
from utils.json_utils import JsonUtils


def log_response(func):
    def _log_response(*args, **kwargs) -> requests.Response:
        response = func(*args, **kwargs)

        Logger.info(f"Request: {curlify.to_curl(response.request)}")

        body = (
            json.dumps(response.json(), indent=2)
            if JsonUtils.is_json(response.text)
            else response.text
        )

        Logger.info(
            f"Response status code='{response.status_code}', "
            f"elapsed_time='{response.elapsed}'\n{body}\n"
        )

        return response

    return _log_response


class ApiUtils:
    def __init__(self, url: str, headers=None):
        self.session = Session()
        self.session.headers.update(headers or {})
        self.url = url

    @log_response
    def get(self, endpoint: str, **kwargs):
        resp = self.session.get(self.url + endpoint, **kwargs)
        return resp

    @log_response
    def post(self, endpoint: str, data=None, json=None, **kwargs):
        resp = self.session.post(self.url + endpoint, data=data, json=json, **kwargs)
        return resp

    @log_response
    def put(self, endpoint: str, data=None, json=None, **kwargs):
        resp = self.session.put(self.url + endpoint, data=data, json=json, **kwargs)
        return resp

    @log_response
    def delete(self, endpoint: str, data=None, json=None, **kwargs):
        resp = self.session.delete(self.url + endpoint, data=data, json=json, **kwargs)
        return resp
