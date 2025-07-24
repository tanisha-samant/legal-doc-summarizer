# 📄 Legal Document Analyzer

An AI-powered web app that extracts key legal clauses and generates concise summaries from uploaded legal documents (PDF or TXT). Built with **Python**, **SpaCy**, **NLTK**, **Hugging Face Transformers**, and **Streamlit**.

---

## ✨ Features

- 📂 Upload legal documents in **PDF** or **TXT**
- 🔎 Automatically extract key clauses:
  - Termination
  - Confidentiality
  - Jurisdiction
  - Liability
  - Indemnification
- 🧠 Generate **AI-powered summaries**
- 💡 Built with state-of-the-art **transformers** (BART model)

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- SpaCy  
- NLTK  
- Hugging Face Transformers  
- PyPDF2  

---

## 📁 Project Structure
```
legal_summarizer/
│
├── app.py # Streamlit frontend app
├── utils.py # File reading, clause extraction, summarization logic
├── requirements.txt # Python dependencies
└── sample_legal_document.pdf # Sample legal PDF (optional)
```
---

## 🧪 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/legal-summarizer.git
cd legal-summarizer
```
### 2. Create a virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Download SpaCy language model
```
python -m spacy download en_core_web_sm
```
### 5. Run the Streamlit app
```
streamlit run app.py
```
