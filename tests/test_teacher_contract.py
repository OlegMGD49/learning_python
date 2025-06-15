import random

from faker import Faker

from src.services.university.helpers.teacher_helper import TeacherHelper
from src.services.university.models.base_teacher import SubjectEnum

faker = Faker()


class TestCreateTeacher:

    def test_create_teacher(self, university_base_client_admin):
        teacher_helper = TeacherHelper(base_api_client=university_base_client_admin)
        resp = teacher_helper.post_teacher(json={"first_name": faker.first_name(),
                                                 "last_name": faker.last_name(),
                                                 "subject": random.choice([option for option in SubjectEnum])})
        assert resp.status_code == 201, resp.json()

    def test_get_teacher_by_id(self, university_base_client_admin):
        teacher_helper = TeacherHelper(base_api_client=university_base_client_admin)
        resp = teacher_helper.post_teacher(json={
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "subject": random.choice([option for option in SubjectEnum])
        })

        assert resp.status_code == 201, resp.json()
        teacher_id = resp.json()["id"]
        teacher_first_name = resp.json()["first_name"]
        teacher_subject = resp.json()["subject"]

        resp = teacher_helper.get_teacher_by_id(teacher_id)

        assert resp.status_code == 200, resp.json()
        assert resp.json()["first_name"] == teacher_first_name
        assert resp.json()["subject"] == teacher_subject

    def test_create_teacher_anonym(self, university_base_client_anonym):
        teacher_helper = TeacherHelper(base_api_client=university_base_client_anonym)
        resp = teacher_helper.post_teacher(json={"first_name": faker.first_name(),
                                                 "last_name": faker.last_name(),
                                                 "subject": random.choice([option for option in SubjectEnum])})
        assert resp.status_code == 401, resp.json()

    def test_delete_teacher_by_id(self, university_base_client_admin):
        teacher_helper = TeacherHelper(base_api_client=university_base_client_admin)
        resp = teacher_helper.post_teacher(json={"first_name": faker.first_name(),
                                                 "last_name": faker.last_name(),
                                                 "subject": random.choice([option for option in SubjectEnum])})
        assert resp.status_code == 201, resp.json()
        teacher_id = resp.json()["id"]

        resp = teacher_helper.delete_teacher_by_id(teacher_id)

        assert resp.status_code == 200, resp.json()

        resp = teacher_helper.get_teacher_by_id(teacher_id)

        assert resp.status_code == 404, resp.json()
        assert resp.json()["detail"] == "Teacher not found"
