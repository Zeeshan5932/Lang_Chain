import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()

model = GoogleGenerativeAI(model="gemini-3.5-flash")

st.title("Research Paper Summarizer")


input_text = st.text_input("enter your research paper text here", placeholder="Paste the text of the research paper you want to summarize.")

if st.button("Summarize"):
    if input_text.strip():
        summary = model.invoke(input_text)
        st.write(summary)