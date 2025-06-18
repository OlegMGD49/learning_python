from pydantic import BaseModel, ConfigDict, Field

from enum import IntEnum


class GradeRange:
    MIN_GRADE = 0
    MAX_GRADE = 5


class BaseGrades(BaseModel):
    model_config = ConfigDict(extra="forbid")

    teacher_id: int
    student_id: int
    grade: int = Field(ge=GradeRange.MIN_GRADE, le=GradeRange.MAX_GRADE)
