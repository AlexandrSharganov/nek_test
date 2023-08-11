#!/bin/sh

until cd /app/nek
do
    echo "Waiting for server volume..."
done

celery -A nek worker --loglevel DEBUG --concurrency 1 -E
