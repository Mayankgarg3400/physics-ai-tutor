from langchain_community.document_loaders import PyMuPDFLoader
 
class PDFLoader:  
    # instead of def Load_pdf():  
    # we use PDFLoader  because later we support pdf,txt,docx
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
      
    def load(self):
        loader = PyMuPDFLoader(self.pdf_path)
        documents = loader.load()
        return documents
            
        