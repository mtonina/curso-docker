# syntax=docker/dockerfile:1.4
FROM python:3.10-alpine

WORKDIR /code

COPY requirements.txt /code
COPY app.py /code
COPY start.sh .
RUN <<EOF
pip3 install -r requirements.txt
apk --update add redis
chmod 755 start.sh
EOF


CMD ./start.sh