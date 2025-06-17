import random

from conftest import create_teacher_id
from services.university.models.base_grades import BaseGrades, GradeRange
from services.university.models.grades_request import GradesRequest
from services.university.university_service import UniversityService


class TestGradeCreate:
    def test_create_grade(self, university_api_client_admin, create_teacher_id, created_student_id):
        university_service = UniversityService(api_utils=university_api_client_admin)

        grade = GradesRequest(teacher_id=create_teacher_id,
                              student_id=created_student_id,
                              grade=random.randint(GradeRange.MIN_GRADE,
                                                   GradeRange.MAX_GRADE))
        grade_response = university_service.create_grade(grade_request=grade)

        assert grade_response.student_id == created_student_id
