from langchain_text_splitters import CharacterTextSplitter
# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader('dl-curriculum.pdf')

# docs = loader.load()

text = """
        Artificial Intelligence is transforming many industries around the world. Companies are using AI for customer support, document analysis, automation, and data processing. In customer support, AI can understand user questions and provide quick answers. However, AI applications often need access to company documents and internal information. For example, a company may have an employee handbook containing information about salaries, holidays, leave policies, and company rules. Instead of sending the complete handbook to the AI every time, we can divide the document into smaller meaningful chunks. These chunks can then be stored and searched when an employee asks a question.

"""

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=''
)

# result = splitter.split_documents(text)

result = splitter.split_text(text)
print(result)
# print(result[3].page_content)