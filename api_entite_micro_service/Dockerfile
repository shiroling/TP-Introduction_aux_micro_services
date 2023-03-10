FROM python:3.6
RUN mkdir app
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
RUN PYTHONPATH=/app
CMD ["python3", "-u", "-m", "flask", "run", "--host=0.0.0.0"]