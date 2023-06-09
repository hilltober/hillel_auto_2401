FROM ubuntu

USER root
RUN mkdir project
WORKDIR project

COPY tests ./tests
COPY requirements.txt .

RUN apt-get update
RUN apt-get install apt-utils python3 python3-pip -y
RUN ln /usr/bin/python3 /usr/bin/python
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install --upgrade -r requirements.txt
