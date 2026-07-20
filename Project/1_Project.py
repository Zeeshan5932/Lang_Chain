import streamlit as st
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from pypdf import PdfReader


st.set_page_config(
    page_title="Doucment  Similarty Score", 
    page_icon=":memo:",
    layout="wide",
)

st.title("doucments similarty score")


@st.cache_resource
def load_embeding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    
    )

emdedings = load_embeding_model()

documents = []


upload_file = st.file_uploader("Upload a text file" , type=["txt", "pdf"])

#upload the pdf and text files and read the content
if upload_file is not None:
   
    if upload_file.type == "text/plain":
        content = upload_file.read().decode("utf-8")
        
        
    elif upload_file.type == "application/pdf":
        
        pdf_reader = PdfReader(upload_file)
        content = ""
        for page in pdf_reader.pages:
            content += page.extract_text()
            
            # clean text
            content = " ".join(content.split())
        # st.write(content)
        st.success("PDF uploaded successfully!")
        
        
        

query = st.text_input("Enter your query" , placeholder="Enter your query here...")


if st.button("Search"):
    if query.strip():
        
        
        documents = [content]
        #generate embedding for the query
        query_embedding = emdedings.embed_query(query)
        #generate embeddings for the documents
        docs_embeddings = emdedings.embed_documents(documents)
        
        st.write("Document embeddings generated.")
        # calculate similarity between the query and the documents
        similarities = cosine_similarity([query_embedding], docs_embeddings)[0]
        
        #get best match
        index , score = sorted(
            list(enumerate(similarities)), 
            key=lambda x: x[1])[-1]
        
        st.success("Most similar document found:")
        
        
        #  st.write("### 📄 Result")
        # st.write(documents[index])
        st.markdown("### 📄 Result")
        st.markdown(documents[index])
        
        st.write(f"Similarity Score: {score:.4f}")
        
    else:
        st.warning("Please enter a query to search for similar documents.")