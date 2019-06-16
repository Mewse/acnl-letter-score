FROM python:3.7-alpine

RUN pip install -r requirements.txt
ENTRYPOINT ["python", "server.py"]