import os
import shutil

from RAGConfig import DB_PATH
from RAGConfig import DOCUMENTS_PATH
from RAGConfig import EnvironmentVariables

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

EnvironmentVariables.setEnvironmentVariables()

def save_to_database(chunks, db_path):
    if os.path.exists(db_path):
        shutil.rmtree(db_path)
    database = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory=db_path)

def extract_chunks(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(documents)
    return chunks

def load_documents(documents_path):
    loader = DirectoryLoader(documents_path, glob=["*.md", "*.txt"])
    documents = loader.load()
    return documents

def main():
    print("Reading documents...")
    documents = load_documents(DOCUMENTS_PATH)
    print(f"Documents read: {len(documents)}\n")

    print("Extracting chunks from documents...")
    chunks = extract_chunks(documents)
    print(f"Chunks extracted: {len(chunks)}\n")

    print("Saving chunks to vector database...")
    chunks = save_to_database(chunks, DB_PATH)
    print(f"Chunks saved to: {DB_PATH}")

if __name__ == "__main__":
    main()