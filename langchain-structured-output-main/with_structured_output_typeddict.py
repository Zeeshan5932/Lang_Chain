from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

# schema
class Review(TypedDict):

    # key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]
    

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""Homemade Chicken Biryani Review

I recently tried a homemade chicken biryani from a local family-owned restaurant, and it exceeded my expectations. The rice was perfectly cooked, with each grain remaining separate and full of flavor. The chicken was tender, juicy, and well-marinated, blending beautifully with the aromatic spices.

What impressed me the most was the balance of flavors. It wasn't overly spicy, allowing the rich taste of the herbs and traditional spices to stand out. The serving also came with fresh raita and a tangy salad, which complemented the biryani perfectly and made the meal even more enjoyable.

The portion size was generous and easily enough for one hungry person. The food arrived hot, well-packaged, and fresh, which made the overall experience even better.

The only downside was that it had slightly more oil than I prefer, and I would have liked a larger serving of raita. Other than that, it was an excellent meal that I'd happily order again.

Pros:

* Rich, authentic flavor with perfectly balanced spices
* Tender and flavorful chicken
* Generous portion size
* Fresh ingredients and excellent packaging

Cons:

* Slightly oily
* Raita portion could be larger

Overall, this chicken biryani delivered an authentic, satisfying experience. If you're a fan of flavorful rice dishes with well-seasoned chicken, this is definitely worth trying.

Review by Zeeshan

""")
print(result)
print(result['summary'])