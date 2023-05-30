FROM python:3.10-slim-bullseye

RUN apt-get update
RUN apt-get install -y build-essential
RUN pip install --upgrade pip setuptools
RUN apt-get install -y ffmpeg

RUN mkdir /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt
RUN rm -r /usr/src/app