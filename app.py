import qdrant_client
from llama_index import (
    VectorStoreIndex,
    ServiceContext,
    SimpleDirectoryReader,
)
from llama_index.storage.storage_context import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore

import os
from dotenv import load_dotenv
import openai


load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

documents = SimpleDirectoryReader(input_files=["./data/data.txt"]).load_data()

client = qdrant_client.QdrantClient(
    url=os.getenv("QDRANT_END_POINT"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

service_context = ServiceContext.from_defaults()
vector_store = QdrantVectorStore(client=client, collection_name="story_one")
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index = VectorStoreIndex(
    documents, service_context=service_context, storage_context=storage_context
)

query_engine = index.as_query_engine()
response = query_engine.query("Who won the race")
print(response)
