#! /bin/bash
echo starting server
gunicorn app.patched:app -w 3 -k gevent --bind 0.0.0.0:8000