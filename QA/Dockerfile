FROM python:3.8

WORKDIR /

COPY app/ /app
COPY test/ /test
COPY requirements.txt /
COPY run.py /

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"]
