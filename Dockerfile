FROM python:3.8

WORKDIR /


RUN pip install -r requirements.txt

COPY . /

CMD ["python", "run.py"]