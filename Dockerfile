FROM python:3-onbuild
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD . /src/
