# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# model = ChatOpenAI()

# # 1st prompt -> detailed report
# template1 = PromptTemplate(
#     template='Write a detailed report on {topic}',
#     input_variables=['topic']
# )

# # 2nd prompt 
# template2 = PromptTemplate(
#     template='Write a 5 line summary on the following text. /n {text}',
#     input_variables=['text']
# )

# parser = StrOutputParser()

# chain = template1 | model | parser | template2 | model | parser
# result = chain.invoke({'topic': 'black hole'})
# print(result)



# =================================== jsonoutputparser.py ===================================

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os

load_dotenv()

# Define the model directly using HuggingFaceEndpoint
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  # Make sure this model exists or choose another one
    task="text-generation"  # Moved outside of model_kwargs
)
model = ChatHuggingFace(llm=llm)
# Create parser and template
parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me 5 facts of {topic}\n {format_instruction}',
    input_variables=["topic"],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# prompt = template.format()
# print(prompt)
# # Invoke the model with the prompt
# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser
result = chain.invoke({"topic": "Zeeshan Younas"})
print(result)

