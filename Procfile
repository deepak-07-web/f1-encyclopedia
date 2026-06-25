release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn f1_site.wsgi --bind 0.0.0.0:$PORT
