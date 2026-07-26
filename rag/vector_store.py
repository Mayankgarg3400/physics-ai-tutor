from langchain_chroma import Chroma

# one new folder will create
#its means your physics book ab vector database me index ho chuki hai

# embedding and vector databade hmesha ek sath use hote hain phele embedding generate hota hain phir wahi vector db 


class VectorStore:

    def __init__(self, embedding):
        self.embedding = embedding

    def create(self, documents):
        db = Chroma.from_documents(
            documents=documents,
            embedding=self.embedding,
            persist_directory="chroma_db"
        )
        return db