import os
import streamlit as st
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Set OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI Setup
st.title("YouTube Video Q&A Assistant")
st.write("""
    This app helps you extract insights from YouTube videos using their transcripts.
    Just upload a YouTube video URL, and ask questions related to its content.
""")

# Function to fetch the transcript from YouTube
def fetch_transcript(video_id):
    try:
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id, languages=["en"])

        # Flatten transcript to plain text
        transcript = " ".join(chunk.text for chunk in fetched_transcript)
        return transcript
    except TranscriptsDisabled:
        st.error("No captions available for this video.")
        return None
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None

# Function to split transcript into chunks
def split_transcript(transcript):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])
    return chunks

# Function to create embeddings and vector store
def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = FAISS.from_documents(chunks, embeddings)
    return vector_store

# Streamlit input for YouTube URL
video_url = st.text_input("Enter YouTube Video URL:")

if video_url:
    # Extracting video ID from the YouTube URL
    if "youtube.com/watch?v=" in video_url:
        video_id = video_url.split("v=")[-1].split("&")[0]  # Extract video ID from the URL
    elif "youtu.be/" in video_url:
        video_id = video_url.split("youtu.be/")[-1].split("?")[0]  # For shortened YouTube URLs
    else:
        st.error("Please enter a valid YouTube video URL.")
        video_id = None

    # Proceed if a valid video ID is extracted
    if video_id:
        # Fetch transcript and process it
        transcript = fetch_transcript(video_id)
        if transcript:
            # Step 1b: Indexing (Text Splitting)
            chunks = split_transcript(transcript)
            st.write(f"Transcript split into {len(chunks)} chunks.")

            # Step 1c & 1d: Indexing (Embedding Generation and Storing in Vector Store)
            vector_store = create_vector_store(chunks)
            st.write("Vector store created.")

            # Step 2: Retrieval (Search for relevant documents)
            retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

            # Step 3: Augmentation (Generate answer from relevant context)
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

            prompt = PromptTemplate(
                template="""
                    You are a helpful assistant.
                    Answer ONLY from the provided transcript context.
                    If the context is insufficient, just say you don't know.

                    {context}
                    Question: {question}
                """,
                input_variables=['context', 'question']
            )

            # Input for a question
            question = st.text_input("Ask a question related to the video content:")

            if question:
                # Step 2: Retrieve relevant documents based on the question
                retrieved_docs = retriever.invoke(question)

                # Step 3: Extract context from retrieved docs
                context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)

                # Step 4: Generate the response using LLM
                final_prompt = prompt.invoke({"context": context_text, "question": question})
                answer = llm.invoke(final_prompt)

                st.write(f"Answer: {answer.content}")

            # Building a chain for summarization or general answers
            parallel_chain = RunnableParallel({
                'context': retriever | RunnableLambda(lambda docs: "\n\n".join(doc.page_content for doc in docs)),
                'question': RunnablePassthrough()
            })

            main_chain = parallel_chain | prompt | llm | StrOutputParser()

            # Option to summarize the video
            if st.button('Summarize the video'):
                summary = main_chain.invoke('Can you summarize the video')
                st.write(f"Summary: {summary}")
