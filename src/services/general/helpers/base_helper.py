from src.utils.base_api_client import BaseApiClient


class BaseHelper:
    def __init__(self, base_api_client: BaseApiClient):
        self.base_api_client = base_api_client
