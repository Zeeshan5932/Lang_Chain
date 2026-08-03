# from langchain_openai import ChatOpenAI
# from langchain_anthropic import ChatAnthropic

from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = GoogleGenerativeAI(model="gemini-3.5-flash")

model2 = GoogleGenerativeAI(model="gemini-3.5-flash")

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model2 | parser 

chain = parallel_chain | merge_chain

text = """
Generative AI, sometimes called "gen AI", refers to deep learning models that can create complex original content such as long-form text, high-quality images, realistic video or audio and more in response to a user’s prompt or request.

At a high level, generative models encode a simplified representation of their training data, and then draw from that representation to create new work that’s similar, but not identical, to the original data.

Generative models have been used for years in statistics to analyze numerical data. But over the last decade, they evolved to analyze and generate more complex data types. This evolution coincided with the emergence of three sophisticated deep learning model types:.
"""

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()

