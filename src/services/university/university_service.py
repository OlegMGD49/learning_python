from src.services.general.base_service import BaseService
from src.services.university.helpers import grade_helper
from src.services.university.helpers.grade_helper import GradeHelper
from src.services.university.helpers.group_helper import GroupHelper
from src.services.university.helpers.student_helper import StudentHelper
from src.services.university.helpers.teacher_helper import TeacherHelper
from src.services.university.models.grades_request import GradesRequest
from src.services.university.models.grades_response import GradesResponse
from src.services.university.models.group_request import GroupRequest
from src.services.university.models.group_response import GroupResponse
from src.services.university.models.student_request import StudentRequest
from src.services.university.models.student_response import StudentResponse
from src.services.university.models.teacher_request import TeacherRequest
from src.services.university.models.teacher_response import TeacherResponse
from src.utils.base_api_client import BaseApiClient


class UniversityService(BaseService):
    SERVICE_URL = "http://127.0.0.1:8001"

    def __init__(self, base_api_client: BaseApiClient):
        super().__init__(base_api_client)

        self.group_helper = GroupHelper(self.base_api_client)
        self.student_helper = StudentHelper(self.base_api_client)
        self.teacher_helper = TeacherHelper(self.base_api_client)
        self.grade_helper = GradeHelper(self.base_api_client)

    def create_group(self, group_request: GroupRequest) -> GroupResponse:
        resp = self.group_helper.post_group(json=group_request.model_dump())
        return GroupResponse(**resp.json())

    def create_student(self, student_request: StudentRequest) -> StudentResponse:
        resp = self.student_helper.post_student(json=student_request.model_dump())
        return StudentResponse(**resp.json())

    def create_teacher(self, teacher_request: TeacherRequest) -> TeacherResponse:
        resp = self.teacher_helper.post_teacher(json=teacher_request.model_dump())
        return TeacherResponse(**resp.json())

    def create_grade(self, grade_request: GradesRequest)-> GradesResponse:
        reps = self.grade_helper.post_grade(data=grade_request.model_dump())
        return GradesResponse(**reps.json())