from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import StructuredOutputParser, ResponceSchema
import os

load_dotenv()

# Define the model directly using HuggingFaceEndpoint
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  # Make sure this model exists or choose another one
    task="text-generation"  # Moved outside of model_kwargs
)
model = ChatHuggingFace(llm=llm)

schema =[
    ResponceSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponceSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponceSchema(name='fact_3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    template = 'Give 3 fact about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt = template.invoke({'topic': 'black hole'})
result = model.invoke(prompt)
final_result = parser.parse(result.content)
print(final_result)