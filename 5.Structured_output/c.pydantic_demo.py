from pydantic import BaseModel,EmailStr,Field
from typing import Optional
class student(BaseModel):
    name:str='nitish'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=5,description='a decimal value representing the cgpa of a student')

new_student={'age':'32','email':'aa@gmail.com','cgpa':7}
student=student(**new_student)
print(student)
