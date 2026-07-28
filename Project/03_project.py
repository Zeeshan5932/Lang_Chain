import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# OpenAI Model
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7,
    api_key="YOUR_OPENAI_API_KEY"
)

# System + Human Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional cooking assistant. Suggest easy and tasty recipes."),
    ("human", "{question}")
])

st.title("🍳 AI Cooking Assistant")

user_input = st.text_input("Enter ingredients or ask a cooking question:")

if st.button("Get Recipe"):

    if user_input:

        messages = prompt.format_messages(question=user_input)

        response = llm.invoke(messages)

        st.write("### AI Response")
        st.write(response)

    else:
        st.warning("Please enter your question.")