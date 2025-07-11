from langchain_huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document

class RAGAgent:
    def __init__(self):
        self.embedding_function = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}
        )
        self.vectordb = Chroma(embedding_function=self.embedding_function)

    def add_examples(self, examples: list[str]):
        docs = [Document(page_content=example) for example in examples]
        self.vectordb.add_documents(docs)

    def retrieve_examples(self, query: str, k: int = 3) -> list[str]:
        docs = self.vectordb.similarity_search(query, k=k)
        return [doc.page_content for doc in docs]
