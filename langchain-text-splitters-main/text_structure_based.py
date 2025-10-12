from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv



load_dotenv()


llm = ChatOpenAI()



text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
)

# Perform the split
chunks = splitter.split_text(text)


# process each chunks with openai 
for idx, chunk in enumerate(chunks):
    print(f"--- Processing Chunk {idx + 1} ---")
    print(f"Chunk text:\n{chunk}\n")

    # Pass the chunk to the OpenAI model
    response = llm(chunk)

    # Output the model's response for each chunk
    print(f"OpenAI Model Response:\n{response}\n")



# print(len(chunks))
# print(chunks)