FROM python:3.6.0-alpine

RUN apk update
RUN apk add bash

RUN mkdir /dev_data/
COPY requirements.txt /dev_data/requirements.txt

RUN pip install --no-cache-dir -r /dev_data/requirements.txt

WORKDIR /dev_data/

ENV http_proxy ""
ENV https_proxy ""
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["/bin/bash", "-c"]