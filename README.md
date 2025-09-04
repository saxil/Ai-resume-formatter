# 📄 ResumeGenius AI

> An **AI-powered resume formatting tool** that extracts, cleans, and reformats resumes into professional, recruiter-ready templates using **OCR, NLP, and Large Language Models**.

---

## 🚀 Overview

**ResumeGenius AI** is designed to simplify and modernize the way resumes are handled. Instead of spending hours aligning text and tweaking templates, this tool uses **OCR, LangChain-based agents, and Retrieval-Augmented Generation (RAG)** to:

- Parse and extract text from resumes (PDF/DOCX)  
- Reformat content into **clean, professional templates**  
- Ensure **ATS (Applicant Tracking System)** compliance  
- Export the final polished resume as a **PDF**

Whether you're a student, job seeker, or recruiter, this tool automates the most tedious part of resume preparation.

## ✨ Features

- 📂 **Resume Upload**: Upload resumes in PDF/DOCX format  
- 🔎 **OCR Parsing**: Extract text from resumes, even if poorly formatted  
- 🧠 **AI Agents**:
  - **Parser Agent** – Extracts structured information (education, skills, experience)  
  - **Formatter Agent** – Reformats content into clean templates  
  - **RAG Agent** – Enhances content quality and context retrieval  
  - **PDF Exporter Agent** – Exports resume into a polished PDF  
- 📑 **Customizable Templates** (planned)  
- ⚡ **Fast & Consistent** formatting with minimal user input  

---

## 🛠️ Tech Stack

| Layer            | Tools / Libraries       |
|------------------|-------------------------|
| UI / Entry Point | Streamlit / Python      |
| AI Orchestration | LangChain Agents        |
| LLMs             | OpenAI / OpenRouter     |
| Vector Store     | ChromaDB                |
| OCR              | PyMuPDF / Tesseract     |
| Export           | ReportLab, fpdf         |
| DevOps           | GitHub Actions (CI/CD)  |

## 📂 Repository Structure

```
ResumeGenius-AI/
├── app.py                      # Main entry point
├── requirements.txt             # Dependencies
├── agents/                      # Modular AI agents
│   ├── formatter_agent.py       # Handles reformatting logic
│   ├── ocr_agent.py             # OCR and text extraction
│   ├── parser_agent.py          # Parsing and structuring content
│   ├── pdf_exporter_agent.py    # PDF export logic
│   └── rag_agent.py             # RAG-based improvements
├── chroma_db/                   # Vector DB for embeddings
├── .github/workflows/           # CI/CD pipelines
│   └── python-app.yml
├── PRD – ResumeGenius-AI.txt # Product requirement doc
└── README.md
```

---

## ⚡ Installation & Local Deployment

### 🔧 Prerequisites
- Python 3.10+  
- API keys (OpenAI / OpenRouter for LLMs)  
- Tesseract installed (for OCR support)  

### 📥 Clone the Repository
```bash
git clone https://github.com/saxil/ResumeGenius-AI.git
cd ResumeGenius-AI
```

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔐 Configure Environment Variables
Create a `.env` file in the root directory with:

```
OPENAI_API_KEY=your_openai_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

### ▶️ Run the Application
```bash
streamlit run app.py
```

## 🧠 Workflow

1. User uploads a resume (PDF/DOCX).  
2. **OCR Agent** extracts raw text.  
3. **Parser Agent** organizes extracted content into structured fields (education, experience, skills, etc.).  
4. **Formatter Agent** applies professional formatting rules and ATS-friendly templates.  
5. **RAG Agent** (optional) enhances text quality and retrieves relevant improvements.  
6. **PDF Exporter Agent** generates the final polished resume as a PDF.  

---

## 🔮 Roadmap

- 🎨 Add multiple resume templates.  
- 🌐 LinkedIn import integration.  
- 📊 Generate ATS-compliance reports.  
- 🤝 Cover letter generator.  
- ⚡ Offline model support with Ollama / Hugging Face.  

---

## 🤝 Contributing

Contributions are welcome!  

To contribute:  
1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to your branch:  
   ```bash
   git push origin feature/your-feature
   ```
5. Open a Pull Request.

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io) – for the interactive UI  
- [LangChain](https://www.langchain.com) – for LLM orchestration and agents  
- [OpenAI](https://openai.com) & [OpenRouter](https://openrouter.ai) – for LLMs  
- [Ollama](https://ollama.com) – for local/offline LLM support  
- [ChromaDB](https://www.trychroma.com) – for vector database management  
- [PyMuPDF](https://pymupdf.readthedocs.io/) & [Tesseract](https://github.com/tesseract-ocr/tesseract) – for OCR parsing  
- [ReportLab](https://www.reportlab.com/) – for PDF generation  

---

## ✨ Final Note

Built with 💻, ☕, and a mission to help job seekers shine.  
If you find this project useful, please ⭐ the repo and share it with others!  

Let’s make resumes smarter, cleaner, and recruiter-friendly 🚀
