FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000
COPY run.py .

CMD ["python", "run.py"]
