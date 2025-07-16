import streamlit as st
import os
import logging
from agents.ocr_agent import OCRAgent
from agents.parser_agent import ParserAgent
from pydantic import BaseModel
from agents.rag_agent import RAGAgent
from agents.formatter_agent import FormatterAgent
from agents.pdf_exporter_agent import PDFExporterAgent

# Configure logging
logging.basicConfig(filename='debug.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

st.set_page_config(page_title="SmartResume.AI", page_icon="🤖")

st.title("SmartResume.AI – Intelligent Resume Formatting Assistant")
st.markdown("Upload your resume PDF, select your target job role, and our AI agents will enhance and format it for you.")

st.info("**Important:** For OCR to work, you need to have Tesseract OCR installed on your system. Download it from [here](https://tesseract-ocr.github.io/tessdoc/Installation.html). If you are on Windows, you might need to set the `TESSDATA_PREFIX` environment variable or specify the path in `ocr_agent.py`.")
st.info("**Important:** For PDF export using `pdfkit` (if `weasyprint` fails), you need to have `wkhtmltopdf` installed. Download it from [here](https://wkhtmltopdf.org/downloads.html).")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
openrouter_api_base = st.sidebar.text_input("OpenRouter API Base URL (Optional)", value="https://openrouter.ai/api/v1")
model_name = st.sidebar.text_input("Model Name (e.g., gpt-4o, openrouter/auto)", value="gpt-4o")

# Initialize RAGAgent once
rag_agent = RAGAgent()
rag_agent.add_examples([
    "Strong leadership skills, managed a team of 5 engineers, delivering projects on time and within budget.",
    "Developed and deployed scalable machine learning models that improved prediction accuracy by 15%.",
    "Proficient in Python, Java, and C++ with extensive experience in data structures and algorithms.",
    "Successfully led cross-functional teams to achieve project milestones and exceed client expectations.",
    "Implemented robust testing frameworks, reducing critical bugs by 25% in production environments.",
    "Optimized database queries, resulting in a 30% reduction in data retrieval time.",
    "Designed and developed user-friendly interfaces using React and Angular, enhancing user experience.",
    "Conducted in-depth market research and competitive analysis to identify new product opportunities.",
    "Managed social media campaigns that increased brand engagement by 40% and drove lead generation.",
    "Provided exceptional customer support, resolving complex issues and maintaining high satisfaction rates."
])

uploaded_file = st.file_uploader("📥 Upload your resume (PDF)", type="pdf")
job_role = st.text_input("🎯 Target Job Role (e.g., Data Analyst, Product Manager)")

if st.button("✨ Format Resume"):
    if uploaded_file is not None and job_role and openai_api_key:
        with st.spinner("Processing... Our AI agents are at work! 🧠"):
            try:
                # 1. OCR Agent: Extract raw text
                ocr_agent = OCRAgent()
                pdf_bytes = uploaded_file.read()
                extracted_text = ocr_agent.extract_text_from_pdf(pdf_bytes)
                logging.info("OCR successful.")

                # 2. Parser Agent: Structure into fields
                if not (openai_api_key.startswith('sk-') or openai_api_key.startswith('sk-or-')):
                    st.error("Please enter a valid OpenAI or OpenRouter API key.")
                    st.stop()
                parser_agent = ParserAgent(openai_api_key=openai_api_key, base_url=openrouter_api_base)
                parsed_data = parser_agent.parse_resume(extracted_text)
                logging.info("Parsing successful.")

                # 3. RAG Agent: Retrieve relevant examples
                retrieved_examples = rag_agent.retrieve_examples(job_role)
                logging.info("RAG retrieval successful.")

                # 4. Formatter Agent: Rewrite and format
                formatter_agent = FormatterAgent(openai_api_key=openai_api_key, model_name=model_name, openrouter_api_base=openrouter_api_base)
                formatted_resume_content = formatter_agent.format_resume(
                    parsed_data.dict(), job_role + "\n\nRelevant Examples: " + "\n".join(retrieved_examples)
                )
                logging.info("Formatting successful.")

                # 5. PDF Exporter Agent: Convert to PDF
                pdf_exporter_agent = PDFExporterAgent()
                output_pdf_path = "formatted_resume.pdf"
                pdf_exporter_agent.export_to_pdf(formatted_resume_content, output_pdf_path)
                logging.info("PDF export successful.")

                st.success("Resume formatted successfully!")

            except Exception as e:
                logging.error(f"An error occurred: {e}", exc_info=True)
                st.error(f"An unexpected error occurred. Please check the debug.log file for more details.")
                st.stop()

        st.subheader("📄 Extracted Text (for debugging)")
        st.text_area("Extracted Text", extracted_text, height=300)

        st.subheader("📊 Parsed Data (for debugging)")
        st.json(parsed_data.dict())

        st.subheader("✨ Formatted Resume Preview")
        st.markdown(formatted_resume_content)

        with open(output_pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Formatted Resume (PDF)",
                data=f.read(),
                file_name="formatted_resume.pdf",
                mime="application/pdf",
            )
    else:
        st.error("Please upload a resume, specify the target job role, and provide your OpenAI API Key.")

