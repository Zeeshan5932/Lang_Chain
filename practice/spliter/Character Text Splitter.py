from langchain_text_splitters import CharacterTextSplitter

text = """
LangChain is a framework for building AI applications.
It provides tools for LLMs, prompts, chains and RAG.
"""

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(text)

for chunk in chunks:
    print(chunk)
    print("-----")