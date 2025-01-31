from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import os
import time
from langchain_ollama import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")    
app = FastAPI()

# Add CORS middleware to handle frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_credentials=True,
    allow_methods=["*"],   
    allow_headers=["*"],   
)

# URL processing function
class Query(BaseModel):
    url: str
    prompt: str

# Global variables for storing scraped data and vector store
vector_store = None
last_url = None
text_splitter = None
documents = None
embeddings = None

def scrape_web_page(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = "\n".join([para.get_text() for para in paragraphs])
        return text
    except Exception as e:
        return f"Error: {e}"

@app.post("/process_url")
async def process_url(query: Query):
    global vector_store, last_url, text_splitter, documents, embeddings

    if last_url != query.url:
        scraped_text = scrape_web_page(query.url)

        if "Error" in scraped_text:
            raise HTTPException(status_code=400, detail=scraped_text)

        # Split the text and create documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_text(scraped_text)
        documents = [Document(page_content=doc) for doc in docs]

        # Create embeddings with Ollama
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        vector_store = FAISS.from_documents(documents, embeddings)
        last_url = query.url

    return {"message": "URL processed successfully"}

@app.post("/query")
async def query_system(query: Query):
    if vector_store is None:
        raise HTTPException(status_code=400, detail="Vector store not found. Please process a URL first.")

    llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.2-1b-preview")

    prompt = ChatPromptTemplate.from_template('''
    Answer the questions based on the provided context.
    Please provide accurate response based on the question.
    You can speak english, hindi and mixture of both languages.
    You are a stupid but sweet ai assistant from india.
    You can also add the context on your own to enhance user experience.
    Behave more like human than AI.
    <context>
    {context}
    Question: {input}
    ''')

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector_store.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({"input": query.prompt})
    elapsed_time = time.process_time() - start

    return {"answer": response['answer'], "response_time": elapsed_time}

