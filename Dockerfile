FROM python:3.8-alpine
LABEL maintainer="TECHWIZ"

ENV PYTHONUNBUFFERED 1

RUN mkdir /apple_school_project

WORKDIR /apple_school_project

ADD . /apple_school_project

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
