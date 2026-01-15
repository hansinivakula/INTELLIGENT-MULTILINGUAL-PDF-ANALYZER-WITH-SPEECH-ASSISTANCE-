# admin.py
import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Admin Dashboard", layout="wide")
st.title("📊 Admin Dashboard")

conn = sqlite3.connect("data.db")

docs = pd.read_sql("SELECT * FROM documents", conn)
audio = pd.read_sql("SELECT * FROM audio_history", conn)

st.subheader("📄 Documents")
st.dataframe(docs)

st.subheader("🔊 Audio History")
st.dataframe(audio)
