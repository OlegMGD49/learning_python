import random

import pytest

from services.auth.auth_service import AuthService
from services.auth.models.login_requets import LoginRequest
from services.auth.models.register_request import RegisterRequest

from faker import Faker

from services.university.models.base_student import DegreeEnum
from services.university.models.base_teacher import SubjectEnum
from services.university.models.group_request import GroupRequest
from services.university.models.student_request import StudentRequest
from services.university.models.teacher_request import TeacherRequest
from services.university.university_service import UniversityService
from utils.api_utils import ApiUtils

faker = Faker()


@pytest.fixture(scope="function", autouse=False)
def auth_api_client_anonym():
    api_utils = ApiUtils(url=AuthService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_client_anonym():
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL)
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def access_token(auth_api_client_anonym):
    auth_service = AuthService(auth_api_client_anonym)
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
    api_utils = ApiUtils(url=AuthService.SERVICE_URL,
                         headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def university_api_client_admin(access_token):
    api_utils = ApiUtils(url=UniversityService.SERVICE_URL,
                         headers={"Authorization": f"Bearer {access_token}"})
    return api_utils


@pytest.fixture(scope="function", autouse=False)
def created_group_id(university_api_client_admin):
    university_service = UniversityService(api_utils=university_api_client_admin)

    group = GroupRequest(name=faker.name())
    group_response = university_service.create_group(group_request=group)

    return group_response.id


@pytest.fixture(scope="function", autouse=False)
def created_student_id(university_api_client_admin, created_group_id):
    university_service = UniversityService(api_utils=university_api_client_admin)

    student = StudentRequest(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=faker.email(),
        degree=random.choice([option for option in DegreeEnum]),
        phone=faker.numerify("+7##########"),
        group_id=created_group_id
    )
    student_response = university_service.create_student(student_request=student)

    return student_response.id


@pytest.fixture(scope="function", autouse=False)
def create_teacher_id(university_api_client_admin):
    university_service = UniversityService(university_api_client_admin)
    teacher = TeacherRequest(first_name=faker.first_name(),
                             last_name=faker.last_name(),
                             subject=random.choice([option for option in SubjectEnum]))
    teacher_response = university_service.create_teacher(teacher_request=teacher)

    return teacher_response.id
