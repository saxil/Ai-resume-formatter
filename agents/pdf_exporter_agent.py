import pdfkit
from weasyprint import HTML

class PDFExporterAgent:
    def __init__(self):
        pass

    def export_to_pdf(self, html_content: str, output_path: str):
        # WeasyPrint is generally more robust for HTML to PDF conversion
        HTML(string=html_content).write_pdf(output_path)
        # Alternatively, if weasyprint has issues, pdfkit can be used (requires wkhtmltopdf)
        # pdfkit.from_string(html_content, output_path)
