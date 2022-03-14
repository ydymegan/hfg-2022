import streamlit as st
import pandas as pd
import spacy
import base64
from PIL import Image
from spacy import displacy
from tika import parser
import docx2txt
from pathlib import Path

HTML_WRAPPER_1 = """<div style="overflow-x: auto; background-color: #f0d1d9; border: 2px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem; 
                margin-bottom: 1.5rem">{}</div>"""
HTML_WRAPPER_2 = """<div style="overflow-x: auto; background-color: #FAF9F6; width: min-content; white-space: nowrap; border: 2px solid #543478; border-radius: 0.25rem; padding: 0.5rem; 
                margin-bottom: 1.5rem">{}</div>"""
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
    ruler.from_disk('jz_skill_patterns.jsonl')
    ruler.add_patterns(patterns)
    return nlp_ner

#@st.cache()
def run_nlp(text,model):
    colors = {"SOFT_SKILL": "linear-gradient(90deg, #aa9cfc, #fc9ce7)"}
    options = {"ents": ["SOFT_SKILL"], "colors": colors}
    doc = model(text)
    html = displacy.render(doc, style="ent", options=options)
    html = html.replace("\n", " ")
    st.write(HTML_WRAPPER_1.format(html), unsafe_allow_html=True)

def detect_ents(text, model):
    #colors = {"TECHNICAL_SKILLS": "linear-gradient(90deg, #aba3c2, #d499f2)"}
    #options = {"ents": ["TECHNICAL_SKILLS"], "colors": colors}
    doc = model(text)
    with st.container():
        competencies = []
        for ent in doc.ents:
            if ent.label_ == 'COMPETENCY':
                competencies.append(ent.text)
        df=pd.DataFrame(competencies)
        df['lower']=df[0].apply(lambda x: x.lower())
        for i in df.groupby('lower',sort=True)[0].first().tolist():
            st.write(HTML_WRAPPER_2.format(i.title()), unsafe_allow_html=True)
            
def resume_parse(text):
    detect_ents(resume_text,nlp)
    #slot1.button("Generate Skills", on_click=detect_ents(resume_text,nlp))
    


# img= Image.open("logo.jpeg")
# st.sidebar.image(img, width=300)

st.header("hack for good 2022")
st.caption("Aloysius Chow, Megan Yee, Natalie Chung, Justin Lim")
st.title("Welcome.")

skills_type = st.radio(
     "What skills would you like to detect?",
     ('Soft Skills', 'Technical Skills'))
nlp = load_model()

default_1 = 'I use my problem-solving skills and break down problems into smaller parts. Then, I communicate to my teammates and encourage them to contribute based on their unique skillsets.'
default_2 = 'We were presented with a difficult challenge that was not familiar to the team. I aimed to foster tenacity in the team and keep spirits up so that none of us were discouraged. I did my best to listen actively to each team member\'s concerns and struggles.'
default_3 = 'The situation had remained stagnant for several days, and our manager was on leave and unable to help the team. I showed resilience and continued to persevere, brainstorming for alternative solutions to the problem.'
if skills_type == 'Soft Skills':
    answer_1 = st.text_area("How do you approach problems? What is your process?", default_1, height=10)
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
    data = st.file_uploader("Upload your CV here", type=['pdf', 'docx'])
    resume_text = None
    slot1 = st.empty()
    if data is not None:
        if data.name.endswith('pdf'):
            with st.spinner("Processing..."):
                raw = parser.from_file(data)
                resume_text = raw['content'].lstrip()
        elif data.name.endswith('docx'):
            resume_text = docx2txt.process(data)
        if resume_text:
            resume_parse(resume_text)
        else:
            st.write("Please upload a valid file")
            
        


          
