import streamlit as st
import pandas as pd
import spacy
import base64
from PIL import Image

@st.cache(allow_output_mutation=True)
def load_model():
    pass
    # nlp = spacy.load('skills_model')
    # return nlp

@st.cache()
def run_nlp():
    pass

# img= Image.open("logo.jpeg")
# st.sidebar.image(img, width=300)

st.header("hack for good 2022")
st.caption("Aloysius Chow, Megan Yee, Natalie Chung, Justin Lim")
st.title("Welcome.")

skills_type = st.radio(
     "What skills would you like to detect?",
     ('Soft Skills', 'Technical Skills'))

if skills_type == 'Soft Skills':
    answer_1 = st.text_area("How do you approach problems? What is your process?", height=10)
    answer_2 = st.text_area("Give an example of when you worked well in a team.", height=10)
    answer_3 = st.text_area("What is the most challenging/difficult situation you’ve ever had to resolve, and how did you do it?", height=10)

    
elif skills_type == 'Technical Skills':
    data = st.file_uploader("Upload your CV here", type=['pdf', 'docx'])

    if data is not None:
        pass

st.button("Generate Skills", on_click=run_nlp())


