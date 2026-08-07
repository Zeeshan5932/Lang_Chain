from langchain.text_splitter import CharacterTextSplitter
# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader('dl-curriculum.pdf')

# docs = loader.load()

text = """
        2. 💰 "Aloo Ko 1 Crore Mil Gaye"

Hook:
Bank Manager:
"Congratulations! Aapke account me 1 crore transfer hue hain."

Curiosity:
Sab sochte hain kisne bheje?

Twist:
Galti se kisi ne "Aloo Mattar Gobi Restaurant" ki payment iske account me bhej di."""

splitter = CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(text)
print(result)
# print(result[3].page_content)