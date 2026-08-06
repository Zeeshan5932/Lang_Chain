# from langchain_community.document_loaders import TextLoader
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI()

# prompt = PromptTemplate(
#     template='Write a summary for the following poem - \n {poem}',
#     input_variables=['poem']
# )

# parser = StrOutputParser()

# loader = TextLoader('cricket.txt', encoding='utf-8')

# docs = loader.load()

# print(type(docs))

# print(len(docs))

# print(docs[0].page_content)

# print(docs[0].metadata)

# chain = prompt | model | parser

# print(chain.invoke({'poem':docs[0].page_content}))




# from langchain_community.document_loaders import TextLoader
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import PromptTemplate
# from dotenv import load_dotenv


# load_dotenv()

# # model = ChatOpenAI()
# model = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)
# prompt = PromptTemplate(
#     template= 'Write a Summery for the following poem - \n''{poem}',
#     input_variables=['poem']
# )

# parser = StrOutputParser()

# # Apni text file ka path do
# loader = TextLoader("cricket.txt", encoding="utf-8")

# # Load as Document
# docs = loader.load()



# print(type(docs))              # docs ka type
# print(len(docs))                # kitne documents mile
# print(docs[0].page_content)     # text ka content
# print(docs[0].metadata)         # extra info (like file name)


# chain = prompt | model | parser

# result = chain.invoke({'poem': docs[0].page_content})
# print("\n openai ka result yeh raha\n", result)



from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Model name fixed to gemini-1.5-flash
model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash", 
    temperature=0,
    max_retries=3
)

prompt = PromptTemplate(
    template='Write a Summary for the following poem -\n{poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

# File loading
loader = TextLoader("cricket.txt", encoding="utf-8")
docs = loader.load()

print("Document Type:", type(docs))
print("Total Documents:", len(docs))
print("Metadata:", docs[0].metadata)

# Chain construction and invocation
chain = prompt | model | parser

result = chain.invoke({'poem': docs[0].page_content})
print("\n--- Result ---\n", result)