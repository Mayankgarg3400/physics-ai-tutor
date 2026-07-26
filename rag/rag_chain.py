from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


class RAGChain:

    def __init__(self, llm, retriever):

        self.llm = llm
        self.retriever = retriever

        self.prompt = ChatPromptTemplate.from_template(
            """
You are an expert Physics teacher.

Answer ONLY using the context below.

If the answer is not present in the context, say:

"I couldn't find this information in the uploaded Physics book."

Context:
{context}

Question:
{question}

Answer:
"""
        )

        self.parser = StrOutputParser()

    def invoke(self, question: str):

        docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        chain = (
            self.prompt
            | self.llm
            | self.parser
        )

        answer = chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        return {
            "answer": answer,
            "context": docs
        }