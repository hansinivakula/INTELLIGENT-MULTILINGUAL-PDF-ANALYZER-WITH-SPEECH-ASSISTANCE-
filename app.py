# app.py
import streamlit as st
from backend import *
from ml_model import classify_document
from database import init_db, save_document, save_audio

init_db()
st.set_page_config(layout="wide")
st.title("📄 Multilingual AI-Powered PDF Analyzer")

pdf = st.file_uploader("Upload PDF", type="pdf")

OUTPUT_LANG = {
    "English":"en",
    "Telugu":"te",
    "Hindi":"hi",
    "Tamil":"ta",
    "French":"fr"
}

if pdf:
    text_original = extract_text_from_pdf(pdf.read())

    st.subheader("Extracted Text")
    st.text_area("Extracted Text", text_original, height=250, label_visibility="collapsed")

    detected_lang = detect_language(text_original)
    st.write("Detected Language:", detected_lang)

    # Translate to English for NLP
    text_en = translate_text(text_original, "en") if detected_lang != "en" else text_original

    summary_en = summarize_text_en(text_en)
    keywords_en = extract_keywords_en(text_en)
    category = classify_document(text_en)

    save_document(pdf.name, detected_lang, category, keywords_en, summary_en)

    st.subheader("Analysis (English)")
    st.write("Category:", category)
    st.write("Keywords:", keywords_en)
    st.write("Summary:", summary_en)

    out_lang = st.selectbox("Choose Output Language", OUTPUT_LANG.keys())
    out_code = OUTPUT_LANG[out_lang]

    summary_out = translate_text(summary_en, out_code) if out_code != "en" else summary_en
    keywords_out = translate_text(keywords_en, out_code) if out_code != "en" else keywords_en

    st.subheader("Translated Results")
    st.write("Translated Keywords:", keywords_out)
    st.write("Translated Summary:", summary_out)

    if st.button("🔊 Generate Speech"):
        audio = text_to_speech(summary_out, out_code)
        save_audio("Summary", out_lang, audio)
        st.audio(audio, autoplay=True)
