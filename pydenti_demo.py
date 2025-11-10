from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str='nitish' # default value 
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description='a decimal valuer representing the cgpa of the student')


new_student={'age':'32','email':'abc@gmail.com'}
Student=Student(**new_student)
student_dict= dict(Student)
print(student_dict)


