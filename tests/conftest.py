import pytest
import requests

from src.services.auth.auth_service import AuthService
from src.services.auth.models.login_requets import LoginRequest
from src.services.auth.models.register_request import RegisterRequest
from src.services.university.helpers.group_helper import GroupHelper
from src.services.university.university_service import UniversityService

from faker import Faker

from src.utils.base_api_client import BaseApiClient

faker = Faker()


@pytest.fixture(scope="function", autouse=False)
def auth_base_client_anonym():
    base_api_client = BaseApiClient(base_url=AuthService.SERVICE_URL)
    return base_api_client


@pytest.fixture(scope="function", autouse=False)
def university_base_client_anonym():
    base_api_client = BaseApiClient(base_url=UniversityService.SERVICE_URL)
    return base_api_client


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_base_client_anonym):
    auth_service = AuthService(auth_base_client_anonym)
    username = faker.user_name()
    password = faker.password(length=10,
                              special_chars=True,
                              digits=True,
                              upper_case=True,
                              lower_case=True)
    auth_service.register_user(
        register_request=RegisterRequest(
            username=username,
            password=password,
            password_repeat=password,
            email=faker.email()))
    login_response = auth_service.login_user(login_request=LoginRequest(
        username=username,
        password=password))
    return login_response.access_token


@pytest.fixture(scope="function", autouse=False)
def auth_base_client_admin(access_token):
    base_api_client = BaseApiClient(base_url=AuthService.SERVICE_URL,
                                    headers={"Authorization": f"Bearer {access_token}"})
    return base_api_client


@pytest.fixture(scope="function", autouse=False)
def university_base_client_admin(access_token):
    base_api_client = BaseApiClient(base_url=UniversityService.SERVICE_URL,
                                    headers={"Authorization": f"Bearer {access_token}"})
    return base_api_client


