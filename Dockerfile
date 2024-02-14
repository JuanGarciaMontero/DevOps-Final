FROM python:3.8

WORKDIR /

COPY . .

# Instalar virtualenv y crear un entorno virtual
RUN pip install virtualenv && \
    python -m venv env

# Activar el entorno virtual y realizar la instalación de dependencias
RUN /bin/bash -c "source venv/bin/activate && pip install -r requirements.txt"

EXPOSE 5000

# Ejecutar los comandos dentro del entorno virtual
CMD ["/bin/bash", "-c", "source env/bin/activate && python manage.sh && python run.py"]