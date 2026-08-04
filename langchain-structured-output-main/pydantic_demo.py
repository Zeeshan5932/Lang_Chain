# from pydantic import BaseModel, Field
# from typing import Optional

# class Student(BaseModel):

#     name: str = 'zeeshan'
#     age: Optional[int] = None
#     email: str
#     cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')


# new_student = {'age':'32', 'email':'abc'}

# student = Student(**new_student)
# print(student)
# student_dict = dict(student)

# print(student_dict['age'])

# student_json = student.model_dump_json()


from pydantic import BaseModel


class Student(BaseModel):
    name:str
    age : int
new_student = {'name':"zeeshan", 'age': 19  }
# student = Student(**new_student)
print(new_student)
# print(type(new_student))