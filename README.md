# 📄 Intelligent Multilingual PDF Analyzer with Speech Assistance

This project proposes an Intelligent Multilingual PDF Analyzer with Speech 
Assistance, which integrates Optical Character Recognition (OCR), Natural 
Language Processing (NLP), Machine Learning (ML), and Text-to-Speech (TTS) 
technologies to enable intelligent, accessible, and user-friendly document analysis. 
The application converts text into audio, making documents usable for visually impaired users.

---

## 🎯 Objective
The objective of this project is to design a multilingual PDF analyzer that not only extracts and processes text but also enhances accessibility for visually impaired users. By combining OCR, NLP, ML, and TTS technologies, the system provides:
- Accurate text extraction from diverse PDF formats.
- Automatic language detection and translation.
- Summarization and keyword extraction for quick understanding.
- Speech assistance to make documents accessible through audio.

---

## 🚀 Features
- 📑 **PDF Upload & OCR**: Extracts text from PDFs using Tesseract OCR (supports multiple languages).
- 🌐 **Language Detection & Translation**: Automatically detects language and translates to target languages.
- 📝 **Summarization & Keywords**: Generates concise summaries and extracts key terms.
- 🔊 **Text-to-Speech**: Converts text into audio using gTTS.
- ♿ **Accessibility**: Provides speech assistance for visually impaired users.
- 📊 **Admin Dashboard**: View document and audio history stored in SQLite.

---

## 🛠️ Technologies Used
- **Frontend**: Streamlit (interactive web app)
- **Backend**: Python
- **OCR**: Tesseract OCR, Poppler
- **NLP & ML**: NLTK, langdetect, scikit-learn (for classification tasks)
- **Translation**: Googletrans
- **Text-to-Speech**: gTTS
- **Database**: SQLite

---

## 🔄 Workflow
1. **Upload PDF** → User uploads a PDF file via the Streamlit interface.
2. **OCR Processing** → Text is extracted using Tesseract OCR and Poppler.
3. **Language Detection** → The system identifies the language of the extracted text.
4. **Translation** → Text is translated into the desired target language.
5. **Summarization & Keywords** → NLP techniques generate summaries and extract key terms.
6. **Text-to-Speech** → The processed text is converted into audio using gTTS.
7. **Admin Dashboard** → All documents and audio outputs are logged in SQLite for history tracking.

---

## 🔮 Future Enhancements
- ☁️ **Cloud Deployment**: Host the app on Streamlit Cloud, Heroku, or AWS.  
- 🧠 **Advanced Summarization**: Use transformer-based models (e.g., BERT, GPT).  
- 🎙️ **Voice Commands**: Enable speech input for hands-free accessibility.  
- 📂 **Multi-format Support**: Extend beyond PDFs to Word, images, and handwritten notes.  
- ♿ **Improved Accessibility**: Add customizable speech speed, pitch, and voice options.  
- 🔐 **User Authentication**: Implement login and role-based access.  
- 📈 **Analytics Dashboard**: Track usage statistics and insights.  
- 📱 **Mobile App Integration**: Build Android/iOS versions.  
- 🤝 **Collaboration Features**: Share analyzed documents and audio outputs.  
- 🛡️ **AI-Powered Error Handling**: Detect and fix OCR/translation errors automatically.  

---

### 🖥️ System Requirements
- Operating System: Windows 10/11 (tested), Linux, or macOS
- Python: 3.10 or above

### 📦 Python Environment
Create a virtual environment:
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/username/INTELLIGENT-MULTILINGUAL-PDF-ANALYZER-WITH-SPEECH-ASSISTANCE-.git
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

     