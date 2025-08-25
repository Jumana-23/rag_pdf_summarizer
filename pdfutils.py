# cleaning text function 
import re 
def clean_text(text:str) -> str:
    text = text.strip()
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"Page\s*\d+", " " , text) 
    text = re.sub(r"Page[\s:\.]*\d+(\s*of\s*\d+)?", " ", text)
    text = re.sub(r"\[\d+\]", "", text)  # citation cleanup
    text = re.sub(r"\(.*?\)", "", text)  # remove noisy parentheticals (use with caution!)

    return text 
def extract_chunks_from_pdf(path_to_pdf, chunk = 300) : 
    