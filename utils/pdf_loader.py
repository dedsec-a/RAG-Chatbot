from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import tempfile

# Function to Load the Pdf and Split the Docs 

def split_pdf(file_content):
    with tempfile.NamedTemporaryFile(delete=False,suffix='.pdf') as temp_file:
     temp_file.write(file_content)
     temp_path = temp_file.name


    loader = PyPDFLoader(temp_path)
    documents = loader.load()

    spliter = RecursiveCharacterTextSplitter(chunk_size= 1000,chunk_overlap = 50)
    split_docs = spliter.split_documents(documents=documents)
    return split_docs