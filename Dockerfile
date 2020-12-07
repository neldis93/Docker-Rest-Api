FROM python:3.8.5

ENV PYTHONUNBUNFFERED 1
RUN mkdir /code

WORKDIR /code

COPY . /code/

RUN pip3 --no-cache-dir install -r requirements.txt

