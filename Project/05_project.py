from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional, Literal

load_dotenv()

# -----------------------------
# Create Chat Model
# -----------------------------
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

# -----------------------------
# Structured Output Schema
# -----------------------------
class Review(BaseModel):
    summary: str = Field(description="Short summary of the review")
    sentiment: Literal["Positive", "Negative", "Neutral"] = Field(
        description="Sentiment of the review"
    )
    pros: List[str] = Field(description="List all advantages")
    cons: List[str] = Field(description="List all disadvantages")
    recommendation: str = Field(description="Should someone buy this product?")
    reviewer: Optional[str] = Field(default=None, description="Reviewer's name")

# -----------------------------
# Output Parser
# -----------------------------
parser = PydanticOutputParser(pydantic_object=Review)

# -----------------------------
# Prompt
# -----------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Product Review Analyzer.

Analyze the user's review carefully.

{format_instructions}
            """
        ),
        (
            "human",
            """
Review:

{review}
            """
        ),
    ]
)

# -----------------------------
# Chain
# -----------------------------
chain = prompt | llm | parser

# -----------------------------
# User Review
# -----------------------------
review = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos.

The battery easily lasts a full day.

The 200MP camera is amazing.

However, the phone is very expensive and a little heavy.

Review by Zeeshan Younas.
"""

# -----------------------------
# Invoke
# -----------------------------
result = chain.invoke(
    {
        "review": review,
        "format_instructions": parser.get_format_instructions(),
    }
)

# -----------------------------
# Output
# -----------------------------
print("Summary:")
print(result.summary)

print("\nSentiment:")
print(result.sentiment)

print("\nPros:")
print(result.pros)

print("\nCons:")
print(result.cons)

print("\nRecommendation:")s
print(result.recommendation)

print("\nReviewer:")
print(result.reviewer)