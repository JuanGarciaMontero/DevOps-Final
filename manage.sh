#!/bin/bash

# Requires the database to be up.

FLASK_ENV=coverage
DATABASE_URI=postgresql://postgres:postgres@0.0.0.0:5432/ejer_final
SECRET_KEY=secret
FLASK_COVERAGE=1

python manage.py