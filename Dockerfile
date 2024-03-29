FROM python:3.8

WORKDIR /app
COPY . /app

CMD [/bin/bash -c "pip install -r requirements.txt", "python", "run.py"]