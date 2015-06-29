#!/bin/bash -e

# ToDo: Switch to nosetests

echo "Running unit tests..."
cd pylacuna/tests/
python test_session.py
python test_status.py
python test_body.py

