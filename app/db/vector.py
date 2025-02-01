from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from dotenv import load_dotenv
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_mongodb.index import create_fulltext_search_index
from pymongo import MongoClient

class Vectorize():
    def __init__(self):
        self.docs = None
        load_dotenv()
        self.__google_api_key = os.getenv("GEMINI_API_KEY")
        self.__atlas_key = os.getenv("ATLAS_CONNECTION_STRING")
        self.__db_name = os.getenv("DB_NAME")
        self.__collection_name = os.getenv("COLLECTION_NAME")
        self.__vector_name = os.getenv("VECTOR_INDEX")
    
    def client_setup(self):
        collection = None
        client = MongoClient(self.__atlas_key)
        database = client[self.__db_name]
        collection_list = database.list_collections()
        if self.__collection_name not in collection_list:
            collection = database[self.__collection_name]
        results = list(collection.list_search_indexs())
        if self.__vector_name not in results:
            embeddings = GoogleGenerativeAIEmbeddings(google_api_key=self.__google_api_key)
            vector_store = MongoDBAtlasVectorSearch(
                collection=collection,
                embedding=embeddings,
                index_name=self.__vector_name,
                relevance_score_fn="cosine",
            )
            vector_store.create_vector_search_index(dimensions=768)

    def chunker(self, urls):
        docs = [WebBaseLoader(url).load() for url in urls]
        docs_list = [item for sublist in docs for item in sublist]
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
            chunk_size=250, chunk_overlap=0
        )
        self.docs = text_splitter.split_documents(docs_list)
        print("chunker fn executed")
    
    def store(self):
        try:
            embeddings = GoogleGenerativeAIEmbeddings(google_api_key=self.__google_api_key)
            client = MongoClient(self.__atlas_key)
            collection = client[self.__db_name][self.__collection_name]
            vector_store = MongoDBAtlasVectorSearch(
                collection=collection,
                embedding=embeddings,
                index_name=self.__vector_name,
                relevance_score_fn="cosine",
            )

            texts = [doc for doc in self.docs]
            vector_store.add_documents(texts)
            print("store fn executed")
            return True
        except Exception as e:
            raise e