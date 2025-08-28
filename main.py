from pdfutils import clean_text, chunk_text, chunks_to_documents

name = "data/llm_research_paper.pdf"
raw_text = open(name).read()
cleaned = clean_text(raw_text)
chunks = chunk_text(cleaned, strategy = "paragraph")
docs= chunks_to_documents(chunks, source = name)

print(docs[1].page_content)
print(docs[1].metadata) 


#turning all the files into documents 


