import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

from pydantic import BaseModel, Field
from typing import Literal, Optional


load_dotenv()


model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)


class RestaurantReview(BaseModel):

    restaurant_name: Optional[str] = Field(
        default=None,
        description="Extract restaurant name if available"
    )

    summary: str = Field(
        description="Write a short summary of the review"
    )

    sentiment: Literal["Positive", "Negative", "Neutral"] = Field(
        description="Identify the sentiment of the review"
    )

    food_quality: str = Field(
        description="Analyze food quality"
    )

    service_quality: str = Field(
        description="Analyze service quality"
    )

    pros: Optional[list[str]] = Field(
        default=None,
        description="Extract positive points from review"
    )

    cons: Optional[list[str]] = Field(
        default=None,
        description="Extract negative points from review"
    )

    recommendation: Literal["Visit Again", "Not Recommended"] = Field(
        description="Give final recommendation"
    )


structured_model = model.with_structured_output(RestaurantReview)


st.set_page_config(
    page_title="Restaurant Review Analyzer"
)


st.title("Restaurant Review Analyzer")


analysis_type = st.selectbox(
    "Select Analysis Type",
    [
        "Normal Analysis",
        "Food Focus",
        "Service Focus"
    ]
)


review = st.text_area(
    "Enter Restaurant Review",
    height=200
)


if st.button("Analyze"):

    if not review.strip():

        st.warning("Please enter a review.")

    elif len(review.split()) < 10:

        st.warning("Please enter a detailed review.")

    else:

        system_message = f"""
You are a restaurant review analyzer.

Analyze the review according to this style:
{analysis_type}

Extract information accurately and return the required structure.
"""

        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=review)
        ]


        with st.spinner("Analyzing..."):

            result = structured_model.invoke(messages)


        st.write("Restaurant Name:")
        st.write(result.restaurant_name)


        st.write("Summary:")
        st.write(result.summary)


        st.write("Sentiment:")
        st.write(result.sentiment)


        st.write("Food Quality:")
        st.write(result.food_quality)


        st.write("Service Quality:")
        st.write(result.service_quality)


        st.write("Pros:")

        if result.pros:
            for item in result.pros:
                st.write("-", item)
        else:
            st.write("No pros found")


        st.write("Cons:")

        if result.cons:
            for item in result.cons:
                st.write("-", item)
        else:
            st.write("No cons found")


        st.write("Recommendation:")
        st.write(result.recommendation)