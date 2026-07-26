#question puchne pr relevant page kon nikalega => retriever
from langchain_chroma import Chroma

class Retriever:
    def __init__(self,embedding):
        self.db = Chroma(
            persist_directory="chroma_db",
            embedding_function=embedding
            
        )
    def get_retriever(self):
        return self.db.as_retriever(
            search_type="similarity",
            search_kwargs={
                "k":5
            }
            
        )    