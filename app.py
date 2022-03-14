import streamlit as st
import pandas as pd
import spacy
import base64
from PIL import Image
from spacy import displacy
from tika import parser
import docx2txt
from pathlib import Path

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; 
                margin-bottom: 2.5rem">{}</div>"""

@st.cache(allow_output_mutation=True)


def load_model():
    with open('terms.txt') as f:
      terms = f.readlines()
    patterns = []
    terms[0].split(' ')
    for i in terms:
      tokens = i.rstrip().split(' ')
      tokens_new = [{"LOWER":j} for j in tokens]
      patterns.append({"label":"SOFT_SKILL","pattern":tokens_new})
    nlp_ner = spacy.load("model-best")
    ruler = nlp_ner.add_pipe("entity_ruler", before = "ner")
    ruler.add_patterns(patterns)
    ruler.from_disk('jz_skill_patterns.jsonl')
    return nlp_ner

#@st.cache()
def run_nlp(text,model):
    colors = {"SOFT_SKILL": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}
    options = {"ents": ["SOFT_SKILL"], "colors": colors}
    doc = model(text)
    html = displacy.render(doc, style="ent", options=options)
    html = html.replace("\n", " ")
    st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)

def detect_ents(text, model):
    colors = {"SOFT_SKILL": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}
    options = {"ents": ["TECHNICAL_SKILLS"], "colors": colors}
    doc = model(text)
    with st.container():
        for ent in doc.ents:
            st.write(ent.text)



def resume_parse(text):
    st.button("Generate Skills", on_click=detect_ents(resume_text,nlp))
    


# img= Image.open("logo.jpeg")
# st.sidebar.image(img, width=300)

st.header("hack for good 2022")
st.caption("Aloysius Chow, Megan Yee, Natalie Chung, Justin Lim")
st.title("Welcome.")

skills_type = st.radio(
     "What skills would you like to detect?",
     ('Soft Skills', 'Technical Skills'))
nlp = load_model()


if skills_type == 'Soft Skills':
    answer_1 = st.text_area("How do you approach problems? What is your process?", height=10)
    run_nlp(answer_1,nlp)
##    doc1 = nlp(answer_1)
##    html1 = displacy.render(doc1, style="ent", options = options)
##    html1 = html1.replace("\n", " ")
##    st.write(HTML_WRAPPER.format(html1), unsafe_allow_html=True)
    answer_2 = st.text_area("Give an example of when you worked well in a team.", height=10)
    run_nlp(answer_2,nlp)
    answer_3 = st.text_area("What is the most challenging/difficult situation you’ve ever had to resolve, and how did you do it?", height=10)
    run_nlp(answer_3,nlp)

    
elif skills_type == 'Technical Skills':
    data = st.file_uploader("Upload your CV here", type=['pdf', 'docx', 'txt'])
    resume_text = None
    if data is not None:
        if data.name.endswith('pdf'):
            raw = parser.from_file(data)
            resume_text = raw['content'].lstrip()
        elif data.name.endswith('docx'):
            resume_text = docx2txt.process(data)
        elif data.name.endswith('txt'):
            resume_text = Path(data).read_text()
        if resume_text:
            resume_parse(resume_text)
        else:
            st.write("Please upload a valid file")
            
        


          
