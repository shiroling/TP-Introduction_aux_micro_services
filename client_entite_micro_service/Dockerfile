FROM python:3.6
RUN mkdir app
EXPOSE 8501
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
CMD ["python", "-m", "streamlit", "run", "client.py"]
# CMD ["streamlit", "run", "client.py" "--server.headless", "true"]