FROM python:3.8

WORKDIR /

COPY . /
RUN pip install virtualenv && \
    python -m venv venv

RUN /bin/bash -c "chmod +x run.py && source venv/bin/activate && pip install -r requirements.txt"

EXPOSE 5000