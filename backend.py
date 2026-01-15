# backend.py
import pytesseract
from pdf2image import convert_from_bytes
import cv2, numpy as np
from langdetect import detect
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from gtts import gTTS
from googletrans import Translator
import nltk, os, time, streamlit as st

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\poppler\poppler-25.12.0\poppler-25.12.0\Library\bin"

# Load ALL supported languages together
OCR_LANGS = "eng+tel+hin+tam+fra"

nltk.download("punkt")
translator = Translator()

# ---------- OCR (AUTO LANGUAGE) ----------
@st.cache_data(show_spinner=False)
def extract_text_from_pdf(pdf_bytes):
    pages = convert_from_bytes(pdf_bytes, poppler_path=POPPLER_PATH, dpi=300)
    text = ""
    for page in pages:
        img = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2GRAY)
        text += pytesseract.image_to_string(
            img,
            lang="eng+tel+hin+tam+fra",
            config="--psm 3"
        )
    return text.strip()

# ---------- LANGUAGE DETECTION ----------
def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

# ---------- TRANSLATION ----------
def translate_text(text, target_lang):
    chunks = [text[i:i+800] for i in range(0, len(text), 800)]
    result = []
    for c in chunks:
        try:
            result.append(translator.translate(c, dest=target_lang).text)
            time.sleep(0.2)
        except:
            result.append(c)
    return " ".join(result)

# ---------- NLP (ENGLISH ONLY) ----------
def extract_keywords_en(text, max_words=12):
    words = [w for w in word_tokenize(text.lower()) if w.isalpha()]
    return ", ".join(list(dict.fromkeys(words))[:max_words])

def summarize_text_en(text, n=3):
    sentences = sent_tokenize(text)
    if len(sentences) <= n:
        return text
    freq = Counter(word_tokenize(text.lower()))
    scores = {}
    for s in sentences:
        for w in word_tokenize(s.lower()):
            scores[s] = scores.get(s, 0) + freq.get(w, 0)
    return " ".join(sorted(scores, key=scores.get, reverse=True)[:n])

# ---------- SPEECH ----------
def text_to_speech(text, lang, filename="speech.mp3"):
    chunks = [text[i:i+400] for i in range(0, len(text), 400)]
    files = []
    for i, c in enumerate(chunks):
        tts = gTTS(c, lang=lang)
        name = f"tmp{i}.mp3"
        tts.save(name)
        files.append(name)
    with open(filename, "wb") as f:
        for file in files:
            f.write(open(file, "rb").read())
            #os.remove(file)
    return filename
