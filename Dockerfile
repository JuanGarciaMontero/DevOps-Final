FROM python:3.8

WORKDIR /app

COPY ../devops-final/requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "run.py"]
