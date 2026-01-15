# ml_model.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "invoice payment bill",
    "resume skills education",
    "research methodology paper",
    "legal contract agreement",
    "medical diagnosis report"
]

labels = ["Invoice", "Resume", "Research", "Legal", "Medical"]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def classify_document(text):
    return model.predict(vectorizer.transform([text]))[0]
