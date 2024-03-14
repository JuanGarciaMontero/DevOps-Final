FROM python:3.8

WORKDIR /

COPY . /

RUN /bin/bash -c "pwd"

COPY requirements.txt /app/

RUN pip install -r app/requirements.txt

CMD ["python", "run.py"]