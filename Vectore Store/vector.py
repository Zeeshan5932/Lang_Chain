from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

documents = [
    "The company was founded in 2015.",
    "Employees receive 24 annual leave days every year.",
    "Office timings are 9 AM to 6 PM.",
    "Employees can work remotely two days per week."
]

vector_store = Chroma.from_texts(
    texts=documents,
    embedding=embeddings,
    collection_name="employee_handbook"
)