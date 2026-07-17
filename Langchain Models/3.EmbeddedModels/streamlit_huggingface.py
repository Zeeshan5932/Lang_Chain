import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Document Similarity Search",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 Document Similarity Search")

# Load Embedding Model
@st.cache_resource
def load_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

embeddings = load_embedding_model()

# Sample Documents
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = st.text_input(
    "Enter your query",
    placeholder="Example: tell me about bumrah"
)

if st.button("Search"):
    if query.strip():

        # Generate Embeddings
        doc_embeddings = embeddings.embed_documents(documents)
        query_embedding = embeddings.embed_query(query)

        # Calculate Similarity
        scores = cosine_similarity([query_embedding], doc_embeddings)[0]

        # Get Best Match
        index, score = sorted(
            list(enumerate(scores)),
            key=lambda x: x[1]
        )[-1]

        st.success("Most Similar Document Found ✅")

        st.write("### 📄 Result")
        st.write(documents[index])

        st.write("### 📊 Similarity Score")
        st.write(f"{score:.4f}")

    else:
        st.warning("Please enter a query.")