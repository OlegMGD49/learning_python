from src.utils.base_api_client import BaseApiClient


class BaseService:
    SERVICE_URL = None
    def __init__(self, base_api_client: BaseApiClient):
        self.base_api_client = base_api_client