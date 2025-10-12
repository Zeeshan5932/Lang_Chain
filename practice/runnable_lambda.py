# from langchain.schema.runnable import RunnableLambda


# def word_counter(text):
#     return len(text.split())


# runnable_word_counter = RunnableLambda(word_counter)

# print(runnable_word_counter.invoke("This is a test sentence."))




from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda


load_dotenv()


prompt  = PromptTemplate(
    template= 'write a joke about {topic}',
    input_variables= ['topic']
)


model = ChatOpenAI()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(lambda x: len(x.split()))
    
    })

finall_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = finall_chain.invoke({'topic': 'cricket'})

final_result = """{} \n word count: {}""".format(result['joke'], result['word_count'])

print(final_result)


