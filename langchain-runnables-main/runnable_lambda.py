# # why we use RunnableLambda

# # RunnableLambda is used to create a lambda function that can be executed within the LangChain framework.
# # It allows us to define custom processing logic that can be easily integrated into a larger chain of operations.
# # In this example, we use RunnableLambda to count the number of words in the generated joke.

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv
# from langchain_core.runnables import RunnableSequence, RunnableLambda, RunnablePassthrough, RunnableParallel

# load_dotenv()

# def word_count(text):
#     return len(text.split())

# prompt = PromptTemplate(
#     template='Write a joke about {topic}',
#     input_variables=['topic']
# )

# model = ChatOpenAI()

# parser = StrOutputParser()

# joke_gen_chain = RunnableSequence(prompt, model, parser)

# parallel_chain = RunnableParallel({
#     'joke': RunnablePassthrough(),
#     'word_count': RunnableLambda(word_count)
# })

# final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# result = final_chain.invoke({'topic':'AI'})

# final_result = """{} \n word count - {}""".format(result['joke'], result['word_count'])

# print(final_result)



from langchain_core.runnables import RunnableLambda


def word_count(text):
    return len(text.split())


runnables_lambda = RunnableLambda(word_count)

print(runnables_lambda.invoke("This is a test string to count the number of words."))