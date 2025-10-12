from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # This loads the .env file and sets environment variables

# Assuming OPENAI_API_KEY is set in your .env
model = ChatOpenAI(model="gpt-4" , temperature=0 , max_completion_tokens=100)

result = model.invoke("Tell me the 5 famous resturants in okara")
print(result.content)
