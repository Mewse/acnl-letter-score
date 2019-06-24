FROM python:3.7-alpine
RUN mkdir /server
WORKDIR /server
COPY server .
RUN rm server/client/src
RUN rm server/client/public
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "server.npmpy"]
