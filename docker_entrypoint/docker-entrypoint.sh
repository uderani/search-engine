#!/bin/sh

# Prepare log files and start outputting logs to stdout
source /srv/virtual_python/bin/activate


# Start Gunicorn processes
echo Starting Server.
exec python /srv/search-engine/People/manage.py runserver 0.0.0.0:8000 \
     "$@"
