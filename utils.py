import re
import nltk
import spacy
import PyPDF2
from io import StringIO
from nltk.tokenize import sent_tokenize
from transformers import pipeline

nltk.download('punkt')
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def read_file(file):
    if file.name.endswith('.pdf'):
        return read_pdf(file)
    elif file.name.endswith('.txt'):
        return file.read().decode("utf-8")
    else:
        return ""

def read_pdf(uploaded_file):
    try:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text.strip()
    except Exception as e:
        print("⚠️ PDF read error:", e)
        return ""

def extract_clauses(text):
    sentences = sent_tokenize(text)
    keywords = ['termination', 'liability', 'confidentiality', 'jurisdiction', 'indemnification']
    clauses = []

    for sent in sentences:
        for key in keywords:
            if key in sent.lower():
                clauses.append((key.title(), sent.strip()))
    return clauses

def summarize_text(text):
    text = text[:3000]  # Limit for summarization model
    try:
        summary = summarizer(text, max_length=150, min_length=40, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print("⚠️ Summarization failed:", e)
        return "Summary not available."
