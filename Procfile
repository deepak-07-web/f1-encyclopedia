release: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py add_drivers && python manage.py add_more_data && python manage.py add_final_details && python manage.py add_comprehensive_data
web: gunicorn f1_site.wsgi --bind 0.0.0.0:$PORT
