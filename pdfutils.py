# cleaning text function 
import re 
# the function line simply hints that the received text is a string and 
# the output will also be a string 
def clean_text(text:str) -> str:
    text = text.strip()
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"Page\s*\d+", " " , text) 
    text = re.sub(r"Page[\s:\.]*\d+(\s*of\s*\d+)?", " ", text)
    text = re.sub(r"\[\d+\]", "", text)  # citation cleanup
    text = re.sub(r"\(.*?\)", "", text)  # remove noisy parentheticals (use with caution!)

    return text 
""" line below is called a function signature 
    text: str -> first parameter is a string text 
    strategy: str = "paragraph" -> if user doesnt specify how to chunk we assume default is paragraph 
    chunk_size : int = 200 -> another default parameter 
    list[dict] -> return type annotation 
    """
def chunk_text(text: str, strategy: str = "paragraph", chunk_size: int = 200) -> list[dict]:
    
 
    