from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name:str='nitish'
    age:Optional[int]=None

new_student={}
Student=Student(**new_student)
print(Student.name)