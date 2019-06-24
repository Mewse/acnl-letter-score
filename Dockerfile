FROM python:3.7-alpine
RUN mkdir /server
WORKDIR /server
COPY server .
RUN rm -r client/src
RUN rm -r client/public
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "server.py"]
