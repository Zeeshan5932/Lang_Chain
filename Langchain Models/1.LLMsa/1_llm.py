from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


llm = OpenAI(model="gpt-3.5-turbo-instruct")

# use invoke method to generate text and why we use
# the invoke method is to make the code more readable
# and to make the code more understandable
result = llm.invoke("Hello, my name is John and I am a software engineer. I am working on a project to build a new programming language. I need your help to generate some code examples for me. Can you help me with that?")

print(result)