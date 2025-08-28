# cleaning text function 
import re 
from langchain.docstore.document import Document 
from langchain.text_splitter import RecursiveCharacterTextSplitter 
DATA_PATH = "data/alice_in_wonderland.md"

def clean_text (text:str)->str: 
    text = text.strip()
    text = text.replace("/n", " ") 
    text = re.sub(r"\s+", " " , text) 
    text = re.sub(r"Page\s*\d+", " " , text) 
    return text 


def chunk_text ( text:str, strategy: str = "paragraph", chunk_size: int = 300) -> list[dict]:

    paragraphs = text.split("\n\n") if strategy == "paragraph" else text.split(". ")

    chunks=[]
    for i , chunk in enumerate(paragraphs):
        cleaned = clean_text(chunk)
        if len(cleaned.strip())>0: 
            chunks.append({"text":cleaned, "chunk_id": i})
        return chunks
    
def chunks_to_documents(chunks:list[dict], source:str) -> list[Document]:
    documents = []
    for chunk in chunks:
        documents.append(
            Document(
                page_content= chunk["text"], metadata ={"source":source, "chunk_id": chunk["chunk_id"]}
            )
        )
    return documents 

