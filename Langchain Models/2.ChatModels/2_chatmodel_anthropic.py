from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()


model = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

results = model.invoke("what is the capital of pakistan?")

print(results)  # Should print "Islamabad"

print(os.getenv("ANTHROPIC_API_KEY"))