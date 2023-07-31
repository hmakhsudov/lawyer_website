#!/bin/sh

python manage.py migrate --no-input
python manage.py collectstatic --no-input

# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

gunicorn lawyer_website.wsgi:application --bind 0.0.0.0:8000