# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader('runnables.pdf')

# docs = loader.load()

# print(len(docs))

# print(docs[1].page_content)
# print("\Meta data is here" , docs[1].metadata)


from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load PDF
loader = PyPDFLoader("runnables.pdf")
docs = loader.load()

# Combine all pages into one text
pdf_text = "\n\n".join([doc.page_content for doc in docs])

# Gemini Model
llm = GoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer the user's question only using the PDF content below.

PDF Content:
{pdf}

Question:
{question}
""")

# Create Chain
chain = prompt | llm

# User Question
question = input("Ask a question about the PDF: ")

# Get Answer
response = chain.invoke({
    "pdf": pdf_text,
    "question": question
})

print("\nAnswer:\n")
print(response.content)