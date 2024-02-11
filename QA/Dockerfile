FROM python:3.8

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y postgresql-client

EXPOSE 5000

CMD ["python"]
