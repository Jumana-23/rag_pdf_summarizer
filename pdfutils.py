# cleaning text function 
import re 
from langchain.document_loaders import DirectoryLoader
DATA_PATH = "data/alice_in_wonderland.md"


def load_documents(): 
    loader = DirectoryLoader(DATA_PATH, glob = "*.md")
    documents = loader.load()
    return documents 
def split_text(documents: list[Document]):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000, 
        chunk_overlap = 500, 
        length_function = len , 
        add_start_index = True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.") 
    document = chunks [10]
    print(document.page_content)
    print(document.metadata)
    return chunks 
