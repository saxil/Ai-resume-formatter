from weasyprint import HTML

class PDFExporterAgent:
    def __init__(self):
        pass

    def _create_html_template(self, content: str) -> str:
        return f"""<!DOCTYPE html>
<html>
<head>
<title>Formatted Resume</title>
<style>
    body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
    h1 {{ font-size: 24px; color: #333; border-bottom: 2px solid #333; padding-bottom: 10px; margin-bottom: 20px; }}
    h2 {{ font-size: 20px; color: #555; border-bottom: 1px solid #ccc; padding-bottom: 5px; margin-top: 25px; margin-bottom: 10px; }}
    p {{ margin-bottom: 10px; }}
    ul {{ list-style-type: disc; padding-left: 20px; }}
    li {{ margin-bottom: 5px; }}
    .contact-info {{ text-align: center; margin-bottom: 30px; }}
    .section {{ margin-bottom: 20px; }}
</style>
</head>
<body>
<div class="contact-info">
    {content}
</div>
</body>
</html>"""

    def export_to_pdf(self, formatted_text: str, output_path: str):
        html_content = self._create_html_template(formatted_text)
        HTML(string=html_content).write_pdf(output_path)
