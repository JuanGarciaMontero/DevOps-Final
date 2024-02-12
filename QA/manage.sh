#!/bin/bash

# Requires the database to be up
FLASK_DEBUG=1
export FLASK_DEBUG
export FLASK_ENV=development
export DATABASE_URI=postgresql://postgres:juan@127.0.0.1:5432/ejer_final
export SECRET_KEY=secret
export FLASK_COVERAGE=1

flask test
python manage.py
