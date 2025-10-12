import os
from dotenv import load_dotenv

load_dotenv()
api_token = os.environ.get("OPENAI_API_KEY")
print(api_token)  # Optional: to verify it's loading
