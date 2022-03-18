FROM python:3.9
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY . .
ENV PORT = 
CMD streamlit run /app/app.py --server.port=${PORT} --browser.serverAddress="0.0.0.0"