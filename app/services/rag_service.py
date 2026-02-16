from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader


class RAGService:
    def __init__(self):
        self.vector_store = None
        self._initialize_vector_store()

    def _initialize_vector_store(self):
        loader = TextLoader("app/rag/hospital_docs.txt")
        documents = loader.load()

        splitter = CharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        docs = splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vector_store = FAISS.from_documents(docs, embeddings)

    def retrieve(self, query: str):
        results = self.vector_store.similarity_search(query, k=3)
        return "\n".join([doc.page_content for doc in results])
