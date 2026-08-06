from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.lazy_load()

docs = loader.load()


print(docs[0].page_content) 
print(docs[0].metadata)# Print the first 100 characters of the first document

for document in docs:
    # print(document.metadata)
    print(document.page_content[:100])  # Print the first 100 characters of each document