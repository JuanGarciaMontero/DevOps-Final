#!/bin/bash

# Requires the database to be up
export FLASK_DEBUG=1
export FLASK_ENV=development
export DATABASE_URI=postgresql://postgres:juan@127.0.0.1:5432/ejer_final
export SECRET_KEY=secret

python manage.py
