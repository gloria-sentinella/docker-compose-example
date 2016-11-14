#!/bin/bash
echo $PWD
ls
celery -A celery worker --loglevel=info
python -u app.py

exec "$@"