release: python manage.py makemigrations --no-input
release: python manage.py migrate

web: gunicorn sau_auth_service.wsgi