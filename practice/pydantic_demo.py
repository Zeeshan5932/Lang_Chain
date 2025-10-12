# from pydantic import BaseModel, EmailStr, Field
# # Why we use optional 
# # Optional is used to indicate that a field may or may not be present in the data.
# from typing import Optional

# class student(BaseModel):

#     name : str = "Zeeshan younas"
#     age : Optional[int] = None
#     email :EmailStr
#     cgpa : float = Field(gt=0, le=10)

# new_student = {'age': '20' , 'email':'zeeshanoffical@edu.pk' , 'cgpa': 3.5}

# students = student(**new_student)
# student_dict = dict(students)
# student_json = students.model_dump_json()
# print(student_json)
# # Convert the Pydantic model to a JSON string

from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv


load_dotenv()

#define the model
llm = HuggingFaceEndpoint(
    repo_id = "google/gemma-2-2b-it",
    task = "text-generation"
)


model = ChatHuggingFace(llm=llm)

class Person(BaseModel):

    name: str = Field(description='Name of the person')
    age : int = Field(gt=18, description='age of the person')
    city: str =Field(description='Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
        template= "Generate the name,age and city of a fictional {place} person \n {format_instruction}",
        input_variables=['place'],
        partial_variables={'format_instruction' : parser.get_format_instructions()}

    )

chain = template | model | parser

result = chain.invoke({'place': 'pakistan'})

print(result)