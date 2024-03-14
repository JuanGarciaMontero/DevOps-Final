FROM python:3.8

WORKDIR /app


RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "run.py"]