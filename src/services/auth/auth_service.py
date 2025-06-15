from src.services.auth.helpers.authorization_helper import AuthorizationHelper
from src.services.auth.helpers.user_helper import UserHelper
from src.services.auth.models.login_requets import LoginRequest
from src.services.auth.models.login_response import LoginResponse
from src.services.auth.models.register_request import RegisterRequest
from src.services.general.base_service import BaseService
from src.services.university.models.success_response import SuccessResponse
from src.utils.base_api_client import BaseApiClient


class AuthService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8000"

    def __init__(self, base_api_client: BaseApiClient):
        super().__init__(base_api_client)

        self.authorization_helper = AuthorizationHelper(self.base_api_client)
        self.user_helper = UserHelper(self.base_api_client)

    def register_user(self, register_request: RegisterRequest) -> SuccessResponse:
        resp = self.authorization_helper.post_register(data=register_request.model_dump())
        return SuccessResponse(**resp.json())

    def login_user(self, login_request: LoginRequest) -> LoginResponse:
        resp = self.authorization_helper.post_login(data=login_request.model_dump())
        return LoginResponse(**resp.json())
