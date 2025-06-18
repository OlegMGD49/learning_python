import random
from http.client import responses

from faker import Faker

from services.university.helpers.teacher_helper import TeacherHelper
from services.university.models.base_teacher import SubjectEnum
from services.university.models.error_response import ErrorResponse

faker = Faker()


class TestTeacherContact:
    def test_create_teacher(self, university_api_client_admin):
        teacher_helper = TeacherHelper(api_utils=university_api_client_admin)
        response = teacher_helper.post_teacher(json={"first_name": faker.first_name(),
                                                     "last_name": faker.last_name(),
                                                     "subject": random.choice([option for option in SubjectEnum])})
        assert response.status_code == 201, \
            f"Wrong status code. Actual: '{response.status_code}', but expected: '201'"

    def test_get_teacher_by_id(self, university_api_client_admin, create_teacher_id):
        teacher_helper = TeacherHelper(api_utils=university_api_client_admin)
        response = teacher_helper.get_teacher_by_id(teacher_id=create_teacher_id)

        assert response.status_code == 200, \
            f"Wrong status code. Actual: '{response.status_code}', but expected: '200'"

    def test_delete_teacher(self, university_api_client_admin, create_teacher_id):
        teacher_helper = TeacherHelper(api_utils=university_api_client_admin)
        response = teacher_helper.delete_teacher_by_id(teacher_id=create_teacher_id)

        assert response.status_code == 200, \
            f"Wrong status code. Actual: '{response.status_code}', but expected: '200'"

    def test_get_teacher_after_deleted(self, university_api_client_admin, create_teacher_id):
        teacher_helper = TeacherHelper(api_utils=university_api_client_admin)
        teacher_helper.delete_teacher_by_id(teacher_id=create_teacher_id)

        response = teacher_helper.get_teacher_by_id(teacher_id=create_teacher_id)

        assert response.status_code == 404, \
            f"Wrong status code. Actual: '{response.status_code}', but expected: '404'"

    def test_msg_error_in_get_teacher_after_deleted(self, university_api_client_admin, create_teacher_id):
        teacher_helper = TeacherHelper(api_utils=university_api_client_admin)
        teacher_helper.delete_teacher_by_id(teacher_id=create_teacher_id)

        response = teacher_helper.get_teacher_by_id(teacher_id=create_teacher_id)
        error = ErrorResponse(**response.json())

        assert error.detail == "Teacher not found", \
            f"Wrong text error. Actual: '{error.detail}', but expected: 'Teacher not found'"
