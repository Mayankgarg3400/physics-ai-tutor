# def main():
#     print("Hello from physics-rag!")


# if __name__ == "__main__":
#     main()

# from langchain_ollama import ChatOllama

# llm = ChatOllama(
#     model="qwen2.5:7b",
#     temperature =0
# )
# response = llm.invoke("what is Newton's Second Law?")
# print(response.content)
from langchain_ollama import ChatOllama

from rag.embeddings import EmbeddingModel
from rag.retriever import Retriever
from rag.rag_chain import RAGChain

llm = ChatOllama(
    model="qwen2.5:7b",
    temperature=0,
)

embedding = EmbeddingModel().get_embedding()

retriever = Retriever(embedding).get_retriever()

rag = RAGChain(llm, retriever)

question = input("Ask: ")

answer, docs = rag.ask(question)

print("\nAnswer\n")
print(answer)

print("\nSources\n")

pages = sorted(set(doc.metadata["page"] + 1 for doc in docs))

print(pages)