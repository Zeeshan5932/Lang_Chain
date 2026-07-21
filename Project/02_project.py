import streamlit as st
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from pypdf import PdfReader


st.set_page_config(
    page_title="Document Similarity Score",
    page_icon="memo",
    layout="wide",
)

st.title("Document Similarity Score")

@st.cache_resource
def load_embeded_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    )

embedings = load_embeded_model()

doucments = []

#file upload

uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf"])

if uploaded_file is not None:
    
    if uploaded_file.type == "text/plain":
        content = uploaded_file.read().decode("utf-8")
        
    elif uploaded_file.type == "application/pdf":
        pdf_reader = PdfReader(uploaded_file)
        content = ""
        for page in pdf_reader.pages:
            content += page.extract_text()
        # clean text
        content = " ".join(content.split())
        st.success("PDF uploaded successfully!")
        
query = st.text_input("Enter your query", placeholder="Enter your query here")

if st.button("Search"):
    if query.strip():
        doucments = [content]
        #generate embedding for the query
        query_embedding = embedings.embed_query(query)
        #generate embedding for the documents
        document_embeddings = embedings.embed_documents(doucments)
        #calculate cosine similarity between the query and documents
        similarity_scores = cosine_similarity([query_embedding], document_embeddings)[0]

        
        #get best match
        index , score = sorted(list(enumerate(similarity_scores)), key=lambda x: x[1])[-1]
        
        st.success("Most similar document found:")
        
        
        #  st.write("### 📄 Result")
        # st.write(documents[index])
        st.markdown("### 📄 Result")
        st.markdown(doucments[index])
        
        st.write(f"Similarity Score: {score:.4f}")
        
    else:
        st.warning("Please enter a query to search for similar documents.")
        
        