import streamlit as st
from PyPDF2 import PdfReader
from googletrans import Translator
import openai

#Set OpenAI API key
openai.api_key = "Add OpenAI API Key here"

#Set Streamlit UI Title
st.title("PDF Summarizer & Translator")

#Create File uploader
uploadedFile = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploadedFile is not None:
    #Read PDF content
    pdfReader = PdfReader(uploadedFile)
    pdfText = ""
    for page in pdfReader.pages:
        pdfText += page.extract_text()

    #Display original PDF
    st.subheader("Original PDF")
    st.text(pdfText)

    #Summarize PDF
    st.subheader("Summary")
    summary = openai.Completion.create(
        engine="text-davinci-003",
        prompt=pdfText[:1024],
        temperature=0.5,
        max_tokens=1000,
    )
    st.text(summary.choices[0].text)

    # Translate summary to Sinhala
    st.subheader("Translated Summary into Sinhala")
    translator = Translator()
    translatedSummary = translator.translate(summary.choices[0].text, src="en", dest="si")
    st.text(translatedSummary.text)
