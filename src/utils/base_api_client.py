from requests import Session


class BaseApiClient:
    def __init__(self, base_url: str, headers=None):
        self.session = Session()
        self.session.headers.update(headers or {})
        self.base_url = base_url

    def get(self, endpoint: str, **kwargs):
        resp = self.session.get(self.base_url + endpoint, **kwargs)
        return resp

    def post(self, endpoint: str, data=None, json=None, **kwargs):
        resp = self.session.post(self.base_url + endpoint, data=data, json=json, **kwargs)
        return resp

    def put(self, endpoint: str, data=None, json=None, **kwargs):
        resp = self.session.put(self.base_url + endpoint, data=data, json=json, **kwargs)
        return resp

    def delete(self, endpoint: str, data=None, json=None, **kwargs):
        resp = self.session.delete(self.base_url + endpoint, data=data, json=json, **kwargs)
        return resp
