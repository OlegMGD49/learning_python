import random
from services.university.helpers.grade_helper import GradeHelper
from services.university.models.base_grades import GradeRange


class TestCreateGradeContract:
    def test_create_grade(self, university_api_client_admin, created_student_id, create_teacher_id):
        grade_helper = GradeHelper(api_utils=university_api_client_admin)

        response = grade_helper.post_grade(data={"teacher_id": create_teacher_id,
                                                 "student_id": created_student_id,
                                                 "grade": random.randint(GradeRange.MIN_GRADE,
                                                                         GradeRange.MAX_GRADE)})

        assert response.status_code == 201, \
            f"Wrong status code. Actual: '{response.status_code}', but expected: '201'"
