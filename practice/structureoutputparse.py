from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI()

# Prompt 1: 3 facts
template1 = PromptTemplate(
    template='Give 3 facts about {topic}.\n',
    input_variables=['topic']
)
formatted_prompt1 = template1.format(topic="black hole")
result1 = llm.invoke(formatted_prompt1)

# Prompt 2: 5-line summary
template2 = PromptTemplate(
    template='Write five lines of summary about {topic}.\n',
    input_variables=['topic']
)
formatted_prompt2 = template2.format(topic="black hole")
result2 = llm.invoke(formatted_prompt2)

# Print results
print("=== 3 Facts ===")
print(result1)

print("\n=== 5-line Summary ===")
print(result2)
