from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(
    model="gemini-1.5-pro")

response = model.invoke("what is captial of pakistan?")
print(response)  # Should print "Paris"