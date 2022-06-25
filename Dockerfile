FROM python:3.8.5-slim-buster

RUN apt-get update && apt-get upgrade -y

RUN apt-get install git curl python3-pip ffmpeg -y

RUN python3 -m pip install --upgrade pip

RUN pip3 install -U pip

COPY . /hero/

WORKDIR /hero/

RUN pip3 install -U -r requirements.txt

CMD python3 genStr.py
