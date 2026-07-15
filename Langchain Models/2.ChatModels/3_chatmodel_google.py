from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

# .env file se API Key load karne ke liye
load_dotenv()

# Model ka naam "gemini-2.5-flash" se badal kar "gemini-3.5-flash" kar dein
model = GoogleGenerativeAI(
    model="gemini-3.5-flash"
)

response = model.invoke("what is the capital of pakistan?")
print(response)  # Ab yeh properly "Islamabad" print karega!