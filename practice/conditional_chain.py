from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv
import os

load_dotenv()

# Load API key from .env
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found.")

model = ChatOpenAI(api_key=api_key)

# Output parser
parser = StrOutputParser()

# ✅ Use lowercase values for Literal
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(
        description="Give the sentiment of feedback.")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative:\n{feedback}\n{format_instructions}",
    input_variables=['feedback'],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# Response prompts
prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n{feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n{feedback}",
    input_variables=['feedback']
)

# Branch on sentiment
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment.")
)

# Final chain
chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful mobile phone'}))

# Uncomment the line below to print the graph structure
chain.get_graph().print_ascii()