from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert '),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'Ai Autmoation','topic':'now a days AI automation tools are used in many industries to improve efficiency and productivity.'})

print(prompt)