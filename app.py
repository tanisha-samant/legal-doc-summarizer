import streamlit as st
from utils import read_file, extract_clauses, summarize_text

st.set_page_config(page_title="Legal Document Analyzer", layout="centered")

st.title("📄 Legal Document Analyzer")
st.markdown("Upload a **PDF** or **TXT** legal document to extract key clauses and generate a summary.")

uploaded_file = st.file_uploader("Upload legal document", type=["pdf", "txt"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    # Read content
    with st.spinner("🔍 Reading document..."):
        raw_text = read_file(uploaded_file)

    if not raw_text:
        st.error("❌ Could not read file. Please upload a valid document.")
    else:
        # Clause Extraction
        with st.spinner("🧠 Extracting key clauses..."):
            clauses = extract_clauses(raw_text)

        st.subheader("🔎 Extracted Legal Clauses")
        if clauses:
            for title, content in clauses:
                st.markdown(f"**{title} Clause:**\n> {content}")
        else:
            st.info("No legal clauses found.")

        # Summary
        with st.spinner("✍️ Generating summary..."):
            summary = summarize_text(raw_text)

        st.subheader("📄 Summary")
        st.success(summary)
