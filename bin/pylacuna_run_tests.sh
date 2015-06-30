#!/bin/bash -e

# ToDo: Switch to nosetests

echo "Running unit tests..."
cd pylacuna/tests/
nosetests -s

