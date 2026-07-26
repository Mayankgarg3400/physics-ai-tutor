from langchain_huggingface import HuggingFaceEmbeddings


class EmbeddingModel:

    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(
            #we use dedicated embedding model instead of LLM(owen)
            #this is fast,free and small
            model_name="BAAI/bge-small-en-v1.5",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

    def get_embedding(self):
        return self.embedding