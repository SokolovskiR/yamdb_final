#!/bin/bash

# Collect static files
echo "collect static files"
python manage.py collectstatic --noinput

echo "makemigrations"
python manage.py makemigrations --noinput

echo "Migrate"
python manage.py migrate --noinput

# Start server
echo "starting server ..."
gunicorn api_yamdb.wsgi:application -b :8000
