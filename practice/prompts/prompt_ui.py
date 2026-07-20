from urllib import response

from langchain_google_genai import GoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

model = GoogleGenerativeAI(model="gemini-3.5-flash")

st.header("Research Paper Summarizer")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# make template 
template = PromptTemplate(
    template= """
    You are a research paper summarizer. Your task is to summarize the research paper based on the user's selections.
    
    
    Paper Name: {paper_input}
    Explanation Style: {style_input}
    Explanation Length: {length_input}
     
    1.mathematical details
       - Include relevant mathematical equations and derivations.
       
    2. Analogies and Examples
         - Provide analogies and examples to clarify complex concepts.
         - If the paper includes case studies or practical applications, summarize them as well.
    
    """,
    
    input_variables=["paper_input", "style_input", "length_input"]
    )


# fill the placeholders in the template with user inputs
prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})

# user_input = st.text_input("Enter your prompt:")

if st.button("Summarize"):
    result = model.invoke(prompt)
    
    # print(result)  # Print the response to the console for debugging
    # st.write(result.content)  # Display the response in the Streamlit app
    st.write(result)  # Display the response in the Streamlit app