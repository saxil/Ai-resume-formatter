from pdf2image import convert_from_bytes
import pytesseract

class OCRAgent:
    def __init__(self):
        # You might need to set the path to the Tesseract executable
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pass

    def extract_text_from_pdf(self, pdf_bytes: bytes) -> str:
        text = ""
        images = convert_from_bytes(pdf_bytes)
        for i, image in enumerate(images):
            text += pytesseract.image_to_string(image)
        return text
