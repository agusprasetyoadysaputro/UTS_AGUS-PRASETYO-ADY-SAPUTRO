#!/bin/bash
echo " building project..."
pip install -r requirements.txt
manage.py collectstatic --noinput
echo " build complete"