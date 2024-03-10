# Use an official Python runtime as a parent image
FROM python:3.8

# Install Bash
RUN apt-get update && apt-get install -y bash

# Set the working directory
WORKDIR /

# Copy the current directory contents into the container
COPY . /

# Install virtualenv and create a virtual environment named 'venv'
RUN pip install virtualenv && \
    python -m venv venv

# Activate the virtual environment and install dependencies
RUN /bin/bash -c "chmod +x manage.sh && chmod +x manage.py && chmod +x run.py && source venv/bin/activate && pip install -r requirements.txt"

# Make port 5000 available to the world outside this container
EXPOSE 5000
