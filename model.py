from pydantic import BaseModel

class Todo(BaseModel):
    course_name: str
    year: int
    semester: int
    grade: str
