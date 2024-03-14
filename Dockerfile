FROM python:3.8

WORKDIR /app

RUN /bin/bash -c "pwd"

COPY requirements.txt /app/

RUN pip install -r app/requirements.txt

COPY . /app

CMD ["python", "run.py"]