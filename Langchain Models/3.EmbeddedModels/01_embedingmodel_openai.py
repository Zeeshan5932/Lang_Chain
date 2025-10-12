from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

#get the OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
# Make sure OPENAI_API_KEY is properly set
if not openai_api_key or not openai_api_key.startswith("sk-") or openai_api_key.startswith("sk-proj-"):
    raise ValueError("Please set a valid OPENAI_API_KEY environment variable. The key should start with 'sk-' but not 'sk-proj-'")

# Use model_kwargs for dimension as per warning
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    model_kwargs={"dimensions": 32}
)

result = embeddings.embed_query("what is capital of Pakistan?")
print(str(result))