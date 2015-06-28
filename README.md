# pylacuna
Python api for Lacuna Expanse game

I'm trying to accomplish two things here.

1) Produce generic python libraries for interacting with the Lacuna Expanse game.

2) Use those libraries with some AI to create an automated bot to play the game.


DIRECTORY STRUCTURE
.
├── bin            # scripts
├── pylacuna       # libraries
└── var            # generated files


Installation
------------
To install (tested on Ubuntu 12.04, requires pip):
```
// Clone
git clone https://github.com/miketwo/pylacuna
cd pylacuna
// Create a virtual environment (optional but recommended -- keeps your comp clean)
virtualenv .venv
. .venv/bin/activate
// Install
pip install .
// You should now be able to do this in your own python script:
```
import pylacuna
```
```

Usage
-----
TBD

Development & Test
------------------
To develop and run tests (tested on Ubuntu 12.04):
```
// Clone
git clone https://github.com/miketwo/pylacuna
cd pylacuna
// Create a virtual environment (optional but recommended -- keeps your comp clean)
virtualenv .venv
. .venv/bin/activate
// Install in dev mode
pip install -e .
// Run tests
pylacuna_run_tests.sh
```

ToDo
----
- so many things

Layout
------
Uses a "standard" Python project layout
```
Project/
|-- bin/
|   |-- scripts
|
|-- project/
|   |-- tests/
|   |   |-- __init__.py
|   |   |-- test_library1.py
|   |   |-- test_library2.py
|   |
|   |-- __init__.py
|   |-- library1.py
|   |-- library2.py
|
|-- var/
|   |-- generated files
|
|-- setup.py
|-- README.md
```

# Layers





