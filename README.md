# 📄 Intelligent Multilingual PDF Analyzer with Speech Assistance

A Streamlit mini project that extracts text from PDFs using OCR, detects language, translates, summarizes, and generates speech. Includes an admin dashboard with SQLite for history tracking.

---

## 🚀 Features
- 📑 **PDF Upload & OCR**: Extracts text from PDFs using Tesseract OCR (supports multiple languages).
- 🌐 **Language Detection & Translation**: Automatically detects language and translates to target languages.
- 📝 **Summarization & Keywords**: Generates concise summaries and extracts key terms.
- 🔊 **Text-to-Speech**: Converts text into audio using gTTS.
- 📊 **Admin Dashboard**: View document and audio history stored in SQLite.

---

## 🛠️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python (OCR, NLP, TTS)
- **Libraries**: Tesseract OCR, Poppler, NLTK, Googletrans, gTTS
- **Database**: SQLite

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/hansinivakula/INTELLIGENT-MULTILINGUAL-PDF-ANALYZER-WITH-SPEECH-ASSISTANCE-.git
   cd INTELLIGENT-MULTILINGUAL-PDF-ANALYZER-WITH-SPEECH-ASSISTANCE-
2. Install Dependencies:
   pip install -r requirements.txt
3. Run user app:
   streamlit run app.py
4. Run the admin dashboard:
   streamlit run admin.py

---

# 📂 Project Structure
PDFANALYSER-PROJ/
├── app.py          # User-facing Streamlit app
├── backend.py      # OCR, NLP, translation, speech functions
├── admin.py        # Admin dashboard with SQLite
├── voice_input.py  # Voice input handling
├── data.db         # SQLite database
├── requirements.txt
└── README.md

---

👩‍💻 Author
Developed by Hansini Vakula Daruri
Final-year Computer Science Student

     