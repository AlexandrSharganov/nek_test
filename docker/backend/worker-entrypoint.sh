#!/bin/sh

until cd /app/nek
do
    echo "Waiting for server volume..."
done

# run a worker :)
celery -A nek worker --loglevel=info --concurrency 1 -E
