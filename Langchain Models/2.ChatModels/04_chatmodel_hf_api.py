from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# # Get the Hugging Face API token
huggingface_api_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

# Correct way: pass parameters directly
llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    huggingfacehub_api_token=huggingface_api_token          
         
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("what is capital of Pakistan?")
print(response)
