from faker import Faker
import random

from src.services.university.helpers.group_helper import GroupHelper
from src.services.university.models import group_response
from src.services.university.models.base_student import DegreeEnum
from src.services.university.models.base_teacher import SubjectEnum
from src.services.university.models.grades_request import GradesRequest
from src.services.university.models.group_request import GroupRequest
from src.services.university.models.student_request import StudentRequest
from src.services.university.models.teacher_request import TeacherRequest
from src.services.university.university_service import UniversityService

faker = Faker()


class TestGradeCreate:
    def test_create_grade(self, university_base_client_admin):
        university_service = UniversityService(base_api_client=university_base_client_admin)

        group = GroupRequest(name=faker.name())
        group_resp = university_service.create_group(group_request=group)

        student = StudentRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 email=faker.email(),
                                 degree=random.choice([option for option in DegreeEnum]),
                                 phone=faker.numerify("+7##########"),
                                 group_id=group_resp.id)
        student_resp = university_service.create_student(student_request=student)

        teacher = TeacherRequest(first_name=faker.first_name(),
                                 last_name=faker.last_name(),
                                 subject=random.choice([option for option in SubjectEnum]))
        teacher_resp = university_service.create_teacher(teacher_request=teacher)

        grade = GradesRequest(teacher_id=teacher_resp.id,
                              student_id=student_resp.id,
                              grade=random.randint(0,5))
        grade_resp = university_service.create_grade(grade_request=grade)

        assert grade_resp.teacher_id == teacher_resp.id
        assert grade_resp.student_id == student_resp.id
        assert grade_resp.grade == grade.grade



