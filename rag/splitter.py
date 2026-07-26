from langchain_text_splitters import RecursiveCharacterTextSplitter

#chunking

class TextSplitter:

    def __init__(
        self,
        chunk_size=1000,
        chunk_overlap=200
    ):
        #RecursiveCharacterTextSplitter -> it tries to split in a smart order
        # 1.paragraph(\n\n),line(\n),space(),chracter
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split(self, documents):
        return self.splitter.split_documents(documents)