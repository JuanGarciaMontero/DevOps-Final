FROM python:3.8

WORKDIR /app

COPY requirements.txt /app
RUN pit install -r requirements.txt

COPY . /app

CMD ["python", "run.py"]
