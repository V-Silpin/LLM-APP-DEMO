from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.conversation.memory import ConversationSummaryBufferMemory
from langchain_core.output_parsers import StrOutputParser
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_mongodb.index import create_fulltext_search_index
from pymongo import MongoClient


import os
from dotenv import load_dotenv

class Bot():
    def __init__(self):
        self.retrieval_chain = None
        load_dotenv()
        self.__google_api_key = os.getenv("GEMINI_API_KEY")
        self.__atlas_key = os.getenv("ATLAS_CONNECTION_STRING")
        self.__db_name = os.getenv("DB_NAME")
        self.__collection_name = os.getenv("COLLECTION_NAME")
        self.__vector_name = os.getenv("VECTOR_INDEX")

    def retrieval(self):
        llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=self.__google_api_key)
        embeddings = GoogleGenerativeAIEmbeddings(google_api_key=self.__google_api_key, model="models/embedding-001")
        client = MongoClient(self.__atlas_key)
        collection = client[self.__db_name][self.__collection_name]
        vector_store = MongoDBAtlasVectorSearch(
            collection=collection,
            embedding=embeddings,
            index_name=self.__vector_name,
            relevance_score_fn="cosine",
        )

        prompt = ChatPromptTemplate.from_template(
            """
            Answer the following question based only on the provided context.
            <context>
            {context}
            </context>
            Question: {input}
            """
        )

        document_chain = create_stuff_documents_chain(llm, prompt)

        retriever = vector_store.as_retriever()

        self.retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    def response(self, query):
        response = self.retrieval_chain.invoke({"input": query})
        answer = response['answer']
        return answer