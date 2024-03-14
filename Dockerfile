FROM python:3.8

WORKDIR /

COPY . /
RUN pip install virtualenv && \
    python -m venv venv && \
    source venv/bin/activate && \
    pip install -r requirements.txt

RUN /bin/bash -c "chmod +x run.py"

EXPOSE 5000