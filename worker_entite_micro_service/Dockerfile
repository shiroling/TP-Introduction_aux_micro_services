FROM python:3.6
RUN mkdir app
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
CMD ["python3", "-u", "worker.py"]