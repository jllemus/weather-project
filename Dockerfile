# Pull base image
FROM python:3

RUN apt-get update

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /project
WORKDIR /project

# Install dependencies
COPY requirements.txt /project
RUN pip install -r requirements.txt
COPY . /project
