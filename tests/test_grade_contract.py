import random

from faker import Faker

from src.services.university.helpers.grade_helper import GradeHelper
from src.services.university.helpers.group_helper import GroupHelper
from src.services.university.helpers.student_helper import StudentHelper
from src.services.university.helpers.teacher_helper import TeacherHelper
from src.services.university.models.base_student import DegreeEnum
from src.services.university.models.base_teacher import SubjectEnum

faker = Faker()


class TestCreateGradeContract:

    def test_create_grade(self, university_base_client_admin):
        teacher_helper = TeacherHelper(base_api_client=university_base_client_admin)
        resp = teacher_helper.post_teacher(json={"first_name": faker.first_name(),
                                                 "last_name": faker.last_name(),
                                                 "subject": random.choice([option for option in SubjectEnum])})
        assert resp.status_code == 201, resp.json()
        teacher_id = resp.json()["id"]

        group_helper = GroupHelper(base_api_client=university_base_client_admin)
        resp = group_helper.post_group(json={"name": faker.name()})

        assert resp.status_code == 201, resp.json()
        group_id = resp.json()["id"]

        student_helper = StudentHelper(base_api_client=university_base_client_admin)
        resp = student_helper.post_student(json={"first_name": faker.first_name(),
                                                 "last_name": faker.last_name(),
                                                 "email": faker.email(),
                                                 "degree": random.choice([option for option in DegreeEnum]),
                                                 "phone": faker.numerify("+7##########"),
                                                 "group_id": group_id})

        assert resp.status_code == 201, resp.json()
        student_id = resp.json()["id"]

        grade_helper = GradeHelper(base_api_client=university_base_client_admin)
        resp = grade_helper.post_grade(
            data={"teacher_id": teacher_id, "student_id": student_id, "grade": random.randint(0, 5)})

        assert resp.status_code == 201, resp.json()
