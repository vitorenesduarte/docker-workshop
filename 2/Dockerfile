FROM python:alpine

RUN pip install flask
RUN apk update && apk add curl

COPY app.py /

CMD python app.py ${ID}
