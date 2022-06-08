FROM python:3.7
MAINTAINER Zhaomeiyong
RUN mkdir -p /service/src
WORKDIR /service/src
COPY requirements.txt /service/src
RUN pip install --no-cache-dir -r requirements.txt
COPY . /service/src
EXPOSE 31019
CMD ["python", "main.py"]

