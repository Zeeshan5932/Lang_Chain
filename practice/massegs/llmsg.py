from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import ( 
    SystemMessage,
    HumanMessage,
    AIMessage
)

load_dotenv()

llm =  GoogleGenerativeAI(model="gemini-3.5-flash"
)

messages = [
    SystemMessage(
        content="You are a Python teacher."
    ),
    HumanMessage(
        content="Explain langchain."
    )
]

response = llm.invoke(messages)

messages = messages.append(AIMessage(content=response))

print(messages)