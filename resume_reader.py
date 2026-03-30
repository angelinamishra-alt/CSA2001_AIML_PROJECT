import pdfplumber

def extract_text_from_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            
            if page_text:
                text = text + "\n" + page_text

    return text


def clean_text(text):
    text = text.lower()
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace("-", "")
    
    return text