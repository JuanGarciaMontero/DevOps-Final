FROM python:3.8

WORKDIR /

COPY . /

RUN pip install virtualenv && \
    python -m venv venv && \
    . venv/bin/activate && \
    pip install -r requirements.txt


CMD ["python", "run.py"]