from langchain_ollama import ChatOllama

from rag.embeddings import EmbeddingModel
from rag.retriever import Retriever
from rag.rag_chain import RAGChain


llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0
)

embedding = EmbeddingModel().get_embedding()

retriever = Retriever(
    embedding
).get_retriever()

rag = RAGChain(
    llm,
    retriever
)