@echo off
title Skill Identifier
call C:\Users\aloi\anaconda3\Scripts\activate.bat C:\Users\aloi\anaconda3
call streamlit run app.py
call conda deactivate
pause