# Assignment: LangChain Prompt and Model Integration

# Create a simple AI chatbot using LangChain and Streamlit. In this assignment, you have to create a Prompt Template and connect it with the LLM model you learned earlier. The user should enter a question or message in the Streamlit app, and the prompt should send the user's input to the model to generate a response. Display the final AI-generated response on the Streamlit interface. Keep the project simple and make sure you understand how Prompt Templates, Models, and Streamlit work together.


import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


model = GoogleGenerativeAI(model="gemini-3.5-flash")

prompt_template = PromptTemplate(
    template="""
    You are a helpful assistant. Answer the user's question in a clear and concise manner.
    
    User's Question: {user_input}
    
    Please provide a detailed response.
    """,
    input_variables=["user_input"],
)


user_input = st.text_input("Enter your question or message:")

if st.button("summerize"):
    
    prompt = prompt_template.invoke({'user_input': user_input})
    response = model.invoke(prompt)
    st.write("AI Response:")
    st.write(response)