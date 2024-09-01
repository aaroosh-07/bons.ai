from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from hfQnA import query, API_URL

def load_and_split_doc():
    path = r'.\documents\alchemist.pdf'
    loader = PyPDFLoader(path, extract_images=False)
    docs = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap  = 200,
        length_function = len,
        add_start_index = True,
    )

    chunks = text_splitter.split_documents(docs)
    return chunks

def load_chunks_to_vectorstore(chunks):
    #use embedding to store in chroma db
    #load embedding model
    embedding_model = HuggingFaceEmbeddings()

    db = Chroma.from_documents(chunks, embedding=embedding_model, persist_directory="test-index")
    db.persist()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def retreive_context_vectorDB(question: str):
    #load the vector db
    vectordb = Chroma(persist_directory="test-index", embedding_function=HuggingFaceEmbeddings())
    #load the retriever
    retriever = vectordb.as_retriever(search_type="similarity", search_kwargs = {"k" : 3})
    relvent_docs = retriever.invoke(question)
    context = format_docs(relvent_docs)
    return context

def run_rag():
    choice = input("Do you want to load the document(y/n): ")

    if choice == "y" or choice == "Y":
        chunks = load_and_split_doc()
        load_chunks_to_vectorstore(chunks)

    question = input("Ask any question from document: ")

    context = retreive_context_vectorDB(question)
    model = "distilbert-base-cased"
    payload = {
        "inputs": {
            "question": f"{question}",
            "context": f"{context}",
        }
    }

    url = API_URL[model]

    response = query(payload=payload, api_url=url)

    print(response)

if __name__ == "__main__":
    run_rag()

